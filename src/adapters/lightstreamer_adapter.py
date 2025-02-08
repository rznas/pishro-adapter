import os
import signal
import subprocess
import time
from typing import Sequence

import requests
from lightstreamer.client import *

from src import settings
from src.models import Singleton


class JsServerAdapter(metaclass=Singleton):

    def __init__(self, user_name: str, ls_token: str):
        self.sess = requests.Session()
        self.ls_token = ls_token
        self.user_name = user_name
        self.js_server_process = None
        self.start_server()
        if not self.init_server():
            raise Exception("init failed")

    def init_server(self):
        data = {
            "userName": self.user_name,
            "passWord": self.ls_token,
            "serverAddress": settings.LIGHTSTREAMER_ENDPOINT,
            "adapterSet": "STOCKLISTDEMO_REMOTE",
        }
        _, status_code = self.send_request("post", "init", json=data)
        return status_code == 200

    def start_server(self):
        print("Starting the Express server...")
        self.js_server_process = subprocess.Popen(
            ["node", settings.JS_SERVER_FILE_PATH],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        time.sleep(2)  # Allow some time for the server to start
        print("Server started.")

    def stop_server(self):
        print("Stopping the Express server...")
        os.kill(self.js_server_process.pid, signal.SIGTERM)
        self.js_server_process.wait()  # Wait for the process to terminate
        print("Server stopped.")

    def subscribe_market_index(self):
        data, status_code = self.send_request("post", "/subscribe/market-index")
        if status_code == 500:
            raise Exception(data)
        return status_code == 200

    def subscribe_stock(self, stocks: Sequence[str]):
        data, status_code = self.send_request("post", "/subscribe/stock", json=stocks)
        if status_code == 500:
            raise Exception(data)
        return status_code == 200

    def subscribe_stock_details(self, stocks: Sequence[str]):
        data, status_code = self.send_request(
            "post", "/subscribe/stock-details", json=stocks
        )
        if status_code == 500:
            raise Exception(data)
        return status_code == 200

    def subscribe_market_depth(self, stocks: Sequence[str]):
        data, status_code = self.send_request(
            "post", "/subscribe/market-depth", json=stocks
        )
        if status_code == 500:
            raise Exception(data)
        return status_code == 200

    @staticmethod
    def handle_response(res):
        if res.status_code == 200:
            try:
                return res.json()
            except requests.JSONDecodeError:
                pass
        return {}

    def send_request(
        self,
        method,
        endpoint_relative,
        json=None,
        data=None,
        files=None,
        params=None,
        headers=None,
    ):
        endpoint = os.path.join(
            f"http://localhost:{settings.JS_SERVER_PORT}", endpoint_relative
        )
        res = self.sess.request(
            method, endpoint, params, data, headers, files=files, json=json
        )
        res_data = self.handle_response(res)
        return res_data, res.status_code
