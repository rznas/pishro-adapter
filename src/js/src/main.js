const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const { json } = require("express");
const singletonModel = require("./singleton");
const LightstreamerClient = require('lightstreamer-client-node');
const { LsService, Subscriber } = require('./subscribor');
const createCallback = require("./callbacks");

const app = express();
const PORT = Number(process.env.PORT) || 3000;

app.use(json());


app.get('/', (req, res) => {
    res.send('Lightstreamer Express Server is running.');
});


app.post('/init', (req, res) => {
    const data = req.body;
    const lsClient = new LightstreamerClient.LightstreamerClient(data['serverAddress'], data['adapterSet']);
    lsClient.connectionDetails.setUser(data['userName'])
    lsClient.connectionDetails.setPassword(data['passWord'])
    lsClient.connect();

    try {
        singletonModel.init({
            lsClient: lsClient,
            subscriptions: {},
        });
        res.status(200).send({ message: "Singleton initialized successfully!" });
    } catch (error) {
        res.status(400).send({ error: error.message });
    }
});


app.post('/subscribe/market-index', (req, res) => {

    let data = singletonModel.getData()
    let lastSubscription = data?.marketIndex ?? null;

    try {
        const subscriber = new Subscriber(data?.lsClient);
        data.marketIndex = subscriber.marketIndex(createCallback("market-index"), lastSubscription)
        res.status(200).json({ success: true });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Endpoint for stock
app.post('/subscribe/stock', (req, res) => {
    const { stocks } = req.body;
    let data = singletonModel.getData()
    let lastSubscription = data?.stock ?? null;

    try {
        const subscriber = new Subscriber(data?.lsClient);
        data.stock = subscriber.stock(stocks, createCallback("stock"), lastSubscription)
        res.status(200).json({ success: true });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Endpoint for stockWatchList
app.post('/subscribe/stock-watch-list', (req, res) => {
    const { stocks } = req.body;
    let data = singletonModel.getData()
    let lastSubscription = data?.stockWatchList() ?? null;

    try {
        const subscriber = new Subscriber(data?.lsClient);
        data.stockWatchList = subscriber.stockWatchList(stocks, createCallback("stock-watch-list"), lastSubscription)
        res.status(200).json({ success: true });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Endpoint for stockDetails
app.post('/subscribe/stock-details', (req, res) => {
    const { stocks } = req.body;
    let data = singletonModel.getData()
    let lastSubscription = data?.stockDetails() ?? null;

    try {
        const subscriber = new Subscriber(data?.lsClient);
        data.stockDetails = subscriber.stockDetails(stocks, createCallback("stock-details"), lastSubscription)
        res.status(200).json({ success: true });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Endpoint for realLawInfo
app.post('/subscribe/real-law-info', (req, res) => {
    // const { stocks, callback, oldSubscription } = req.body;
    //
    // try {
    //     const subscription = Subscriber(data?.lsClient).realLawInfo(stocks, callback, oldSubscription);
    //     res.status(200).json({ success: true, subscription });
    // } catch (error) {
    //     res.status(500).json({ success: false, error: error.message });
    // }
});

// Endpoint for stockQueue
app.post('/subscribe/stock-queue', (req, res) => {
    const { stocks } = req.body;
    let data = singletonModel.getData()
    let lastSubscription = data?.stockQueue ?? null;

    try {
        const subscriber = new Subscriber(data?.lsClient);
        data.stockQueue = subscriber.stockQueue(stocks, createCallback("stock-queue"), lastSubscription)
        res.status(200).json({ success: true });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Endpoint for marketDepth
app.post('/subscribe/market-depth', (req, res) => {
    const { stocks } = req.body;
    let data = singletonModel.getData()
    let lastSubscription = data?.marketDepth ?? null;

    try {
        const subscriber = new Subscriber(data?.lsClient);
        data.marketDepth = subscriber.marketDepth(stocks, createCallback("market-depth"), lastSubscription)
        res.status(200).json({ success: true });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Endpoint for orderStateV3
app.post('/subscribe/order-state-v3', (req, res) => {
    const { userName, callback, oldSubscription } = req.body;

    try {
        const subscription = Subscriber.orderStateV3(userName, callback, oldSubscription);
        res.status(200).json({ success: true, subscription });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});


const server = app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});

// Graceful shutdown
process.on("SIGTERM", () => {
    server.close(() => {
        console.log("Server closed gracefully.");
        process.exit(0);
    });
});

module.exports = server;
