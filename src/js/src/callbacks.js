const axios = require('axios');
const {defaults} = require("axios");

function createCallback(dst_endpoint) {
    return {
        onSubscription: () => {
            console.log('Subscription successful');
        }, onUnsubscription: () => {
            console.log('Unsubscribed successfully');
        }, onItemUpdate: (update) => {
            axios.post(`http://localhost:8000/${dst_endpoint}`, update)
                .then(response => {
                    console.log('Data forwarded successfully:', response.data);
                })
                .catch(error => {
                    console.error('Error forwarding data:', error.message);
                });
        }, onSubscriptionError: (code, message) => {
            console.error(`Subscription error: Code=${code}, Message=${message}`);
        }
    }

}

module.exports = createCallback;
