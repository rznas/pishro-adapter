const LightstreamerClient = require('lightstreamer-client-node');


class LsService {
    static SCHEMA = [
        "DateOfEvent",
        "HighPrice",
        "LastTradedPrice",
        "LastTradedPriceVarPercent",
        "LowPrice",
        "TimeOfEvent",
        "TotalNumberOfSharesTraded",
        "TradeDate",
        "VarSign",
        "ClosingPrice",
        "SymbolStateId",
        "BestBuyLimitPrice_1",
        "BestSellLimitPrice_1",
        "BestBuyLimitQuantity_1",
        "BestSellLimitQuantity_1",
        "NumberOfOrdersAtBestBuy_1",
        "NumberOfOrdersAtBestSell_1",
        "BestBuyLimitPrice_2",
        "BestSellLimitPrice_2",
        "BestBuyLimitQuantity_2",
        "BestSellLimitQuantity_2",
        "NumberOfOrdersAtBestBuy_2",
        "NumberOfOrdersAtBestSell_2",
        "BestBuyLimitPrice_3",
        "BestSellLimitPrice_3",
        "BestBuyLimitQuantity_3",
        "BestSellLimitQuantity_3",
        "NumberOfOrdersAtBestBuy_3",
        "NumberOfOrdersAtBestSell_3"
    ];

    constructor(userName = null, client = null) {
        this.client = client;
        this.userName = userName;
    }

    simpleSubscribe(items, fields, updateCallback, subscriptionToUnsubscribe, requestedSnapshot = 'yes') {
        return this.subscriptionToLS(
            'MERGE',
            items,
            fields,
            'TadbirLightRLC',
            requestedSnapshot,
            updateCallback,
            subscriptionToUnsubscribe
        );
    }

    privateSubscribe(mode, fields, updateCallback, subscriptionToUnsubscribe, allItemSubscribed = null) {
        if (!this.userName) {
            throw new Error('userName is required!');
        }
        const items = [
            `${process.env.BROKER_ID}_${this.userName.replace('-', '_').toLowerCase()}_lightrlc`
        ];
        return this.privateSubscribeFull(
            mode,
            fields,
            items,
            'no',
            updateCallback,
            subscriptionToUnsubscribe,
            allItemSubscribed
        );
    }

    privateSubscribeFull(mode, fields, items, requestedSnapshot, updateCallback, subscriptionToUnsubscribe, allItemSubscribed) {
        if (subscriptionToUnsubscribe) {
            this.unSubscription(subscriptionToUnsubscribe);
        }

        fields = fields || [
            "refresh",
            "conditionalalert0",
            "logout",
            "getorders",
            "gettodayorders",
            "getbothorders",
            "onlygetbothorders",
            "getremain",
            "FPCheck",
            "text0"
        ];
        mode = mode || 'RAW';
        let subscription = this.subscriptionToLS(
            mode,
            items,
            fields,
            'TadbirLightPrivateGatewayAdapter',
            requestedSnapshot,
            updateCallback,
            subscriptionToUnsubscribe
        );

        if (allItemSubscribed) {
            const newItems = [`${process.env.BROKER_ID}_lightrlc`];
            subscription = this.subscriptionToLS(
                'RAW',
                newItems,
                fields,
                'TadbirLightPrivateGatewayAdapter',
                'no',
                updateCallback,
                subscriptionToUnsubscribe
            );
        }

        return subscription;
    }

    subscriptionToLS(mode, items, fields, dataAdapter, requestedSnapshot, updateCallback, subscriptionToUnsubscribe) {
        if (subscriptionToUnsubscribe) {
            this.unSubscription(subscriptionToUnsubscribe);
        }

        requestedSnapshot = requestedSnapshot || 'no';
        dataAdapter = dataAdapter || 'TadbirLightRLC';
        fields = fields || LsService.SCHEMA;
        mode = mode || (requestedSnapshot === 'no' ? 'RAW' : 'MERGE');

        if (mode === 'RAW') {
            requestedSnapshot = 'no';
        }

        const subscription = new LightstreamerClient.Subscription(mode, items, fields);
        subscription.setDataAdapter(dataAdapter);
        subscription.setRequestedSnapshot(requestedSnapshot);
        subscription.addListener(updateCallback);
        this.client.subscribe(subscription);
        return subscription;
    }

    unSubscription(subscription) {
        if (subscription) {
            try {
                if (this.client && subscription.isActive()) {
                    this.client.unsubscribe(subscription);
                }
            } catch (error) {
                console.error(error);
            }
        }
    }
}

class Subscriber {

    constructor(client
        // : LightstreamerClient.LightstreamerClient
    ) {
        this.client = client;

    }
    marketIndex(callback, oldSubscription = null) {
        const indexInformationObj = {
            "IRX6XTPI0006": { ISIN: "IRX6XTPI0006", Title: "totalIndex" },
            "IRXZXOCI0006": { ISIN: "IRXZXOCI0006", Title: "farabourseindex" },
            "IRX6XSLC0006": { ISIN: "IRX6XSLC0006", Title: "top50Active" },
            "IRX6XS300006": { ISIN: "IRX6XS300006", Title: "top30Big" },
            "IRXYXTPI0026": { ISIN: "IRXYXTPI0026", Title: "شاخص قیمت (هم وزن)" }
        };

        const items = Object.keys(indexInformationObj).map(key => `${key}_lightrlc`.toLowerCase());
        const fields = [
            "ISIN",
            "SymbolTitle",
            "LastIndexValue",
            "IndexChanges",
            "PercentVariation",
            "DayOfEvent"
        ];

        const lsService = new LsService(null, this.client);
        return lsService.simpleSubscribe(items, fields, callback, oldSubscription, 'yes');
    }

    stock(stocks, callback, oldSubscription = null) {
        const items = stocks.map(stock => `${stock}_lightrlc`.toLowerCase());
        const fields = ["LastTradedPrice", "TradeDate"];

        const lsService = new LsService(null, this.client);
        return lsService.simpleSubscribe(items, fields, callback, oldSubscription);
    }

    stockWatchList(stocks, callback, oldSubscription = null) {
        const items = stocks.map(stock => `${stock}_lightrlc`.toLowerCase());
        const fields = [
            "CompanyName",
            "BasisVolume",
            "PreClosingPrice",
            "FirstTradedPrice",
            "LastTradedPrice",
            "LastTradedPriceVarPercent",
            "TotalNumberOfSharesTraded",
            "ClosingPrice",
            "BestBuyLimitPrice_1",
            "BestSellLimitPrice_1",
            "BestBuyLimitQuantity_1",
            "TotalNumberOfTrades",
            "BestSellLimitQuantity_1",
            "TotalTradeValue",
            "ClosingPriceVarPercent",
            "SymbolStateId",
            "InstrumentCode",
            "LowAllowedPrice",
            "HighAllowedPrice",
            "SymbolHighLimit",
            "SymbolNoteLowLimit"
        ];

        const lsService = new LsService(null, this.client);
        return lsService.simpleSubscribe(items, fields, callback, oldSubscription);
    }

    stockDetails(stocks, callback, oldSubscription = null) {
        const items = stocks.map(stock => `${stock}_lightrlc`.toLowerCase());
        const fields = [
            "HighPrice",
            "TotalNumberOfTrades",
            "TotalTradeValue",
            "LastTradedPrice",
            "LastTradedPriceVar",
            "LastTradedPriceVarPercent",
            "LowPrice",
            "TotalNumberOfSharesTraded",
            "TradeDate",
            "ClosingPrice",
            "SymbolStateId",
            "ClosingPriceVar",
            "ClosingPriceVarPercent",
            "YesterdayPrice"
        ];

        const lsService = new LsService(null, this.client);
        return lsService.simpleSubscribe(items, fields, callback, oldSubscription);
    }

    realLawInfo(stocks, callback, oldSubscription = null) {
        const items = stocks.map(stock => `${stock}_lightrlc`.toLowerCase());
        const fields = [
            "IndInstTrade_Individual_BuyValue",
            "IndInstTrade_Individual_BuyVolume",
            "IndInstTrade_Individual_BuyNumber",
            "IndInstTrade_Individual_SellValue",
            "IndInstTrade_Individual_SellVolume",
            "IndInstTrade_Individual_SellNumber",
            "IndInstTrade_Institutional_BuyValue",
            "IndInstTrade_Institutional_BuyVolume",
            "IndInstTrade_Institutional_BuyNumber",
            "IndInstTrade_Institutional_SellVolume",
            "IndInstTrade_Institutional_SellValue",
            "IndInstTrade_Institutional_SellNumber"
        ];

        const lsService = new LsService(null, this.client);
        return lsService.subscriptionToLS(
            'MERGE',
            items,
            fields,
            '',
            'yes',
            callback,
            oldSubscription
        );
    }

    stockQueue(stocks, callback, oldSubscription = null) {
        const items = stocks.map(stock => `${stock}_lightrlc`.toLowerCase());
        const fields = [
            "BestBuyLimitPrice_1",
            "BestSellLimitPrice_1",
            "BestBuyLimitQuantity_1",
            "BestSellLimitQuantity_1",
            "NumberOfOrdersAtBestBuy_1",
            "NumberOfOrdersAtBestSell_1",
            "BestBuyLimitPrice_2",
            "BestSellLimitPrice_2",
            "BestBuyLimitQuantity_2",
            "BestSellLimitQuantity_2",
            "NumberOfOrdersAtBestBuy_2",
            "NumberOfOrdersAtBestSell_2",
            "BestBuyLimitPrice_3",
            "BestSellLimitPrice_3",
            "BestBuyLimitQuantity_3",
            "BestSellLimitQuantity_3",
            "NumberOfOrdersAtBestBuy_3",
            "NumberOfOrdersAtBestSell_3",
            "BestBuyLimitPrice_4",
            "BestSellLimitPrice_4",
            "BestBuyLimitQuantity_4",
            "BestSellLimitQuantity_4",
            "NumberOfOrdersAtBestBuy_4",
            "NumberOfOrdersAtBestSell_4",
            "BestBuyLimitPrice_5",
            "BestSellLimitPrice_5",
            "BestBuyLimitQuantity_5",
            "BestSellLimitQuantity_5",
            "NumberOfOrdersAtBestBuy_5",
            "NumberOfOrdersAtBestSell_5"
        ];

        const lsService = new LsService(null, this.client);
        return lsService.simpleSubscribe(items, fields, callback, oldSubscription);
    }

    marketDepth(stocks, callback, oldSubscription = null) {
        const items = stocks.map(stock => `${stock}_marketDepth`.toLowerCase());
        const fields = ["data"];

        const lsService = new LsService(null, this.client);
        return lsService.subscriptionToLS(
            'MERGE',
            items,
            fields,
            'MarketDepthAdapter',
            'yes',
            callback,
            oldSubscription
        );
    }

    orderStateV3(userName, callback, oldSubscription = null) {
        const lsService = new LsService(userName, this.client);
        const fields = ["orderstatev6"];

        return lsService.privateSubscribe(
            'MERGE',
            fields,
            callback,
            oldSubscription,
            false
        );
    }
}

module.exports = { LsService, Subscriber };
