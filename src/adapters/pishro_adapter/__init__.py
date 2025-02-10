import base64
import datetime

import cv2
import numpy as np
import pytesseract
import requests
from lightstreamer.client import *

from src import settings
from src.adapters.js_server_adapter import JsServerAdapter
from src.models import Singleton


class PishroAdapter(metaclass=Singleton):

    def __init__(self, login_user_name: str, login_password: str):
        self.sess = requests.Session()
        self.token = None
        self.ls_token = None
        self.ls_client = None
        self.user_name = None
        self.login_user_name = login_user_name
        self.login_password = login_password
        self.js_server_adapter = None

    def get_captcha(self) -> tuple[str, bytes]:
        res = self.send_request("GET", settings.GET_CAPTCHA_ENDPOINT)
        if res.get("IsSuccessfull", False):
            if data := res.get("Data", None):
                if img_b64 := data.get("Captcha", None):
                    img_bytes = base64.b64decode(img_b64)
                    return data.get("CaptchaKey"), img_bytes
        return None, None

    def login(self):
        # captcha
        attempt = 0
        is_login = False
        while not is_login and attempt < 6:
            captcha_code = None
            while captcha_code is None:
                key, image_bytes = self.get_captcha()
                image_array = np.frombuffer(image_bytes, dtype=np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
                image = cv2.dilate(image, np.ones((2, 2), np.uint8))
                image = cv2.erode(image, np.ones((2, 2), np.uint8))
                alpha = 1.7  # Contrast factor
                beta = 0     # No brightness change
                image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
                text = pytesseract.image_to_string(
                    image, config="--psm 6"
                )  # Adjust psm mode if needed
                try:
                    captcha_code = int(text.replace(" ", "").replace("\n", ""))
                    if len(captcha_code) != 4:
                        captcha_code = None
                except:
                    pass
            data = {
                "UserName": self.login_user_name,
                "Password": self.login_password,
                "Captcha": str(captcha_code),
                "CaptchaKey": key,
            }
            res = self.send_request("POST", settings.LOGIN_ENDPOINT, json=data)
            if res.get("IsSuccessfull", False):
                # It is unnecessary because it use cookie and it is by default set in the self.sess
                data = res.get("Data")
                self.token = data.get("Token", None)
                self.ls_token = data.get("LsToken", None)
                self.user_name = data.get("UserName", None)
                is_login = True
            else:
                is_login = False
                attempt += 1
        if is_login:
            self.js_server_adapter = JsServerAdapter(self.user_name, self.ls_token)
        return is_login

    def add_ls_subscriptions(self):
        pass

    def get_portfolio(self):
        res = self.send_request("get", settings.PORTFOLIO_ENDPOINT)
        if res.get("IsSuccessfull", False):
            return res.get("Data")

    def get_all_symbols(self):
        res = self.send_request("get", settings.ALL_SYMBOLS_ENDPOINT)
        return res or []

    def get_all_sectors(self):
        res = self.send_request("get", settings.ALL_SECTORS_ENDPOINT)
        return res or []

    @staticmethod
    def get_symbol_id(symbol):
        return symbol.get("nc", None)

    @staticmethod
    def get_symbol_name(symbol):
        return symbol.get("sf", None)

    def get_symbol_nav_data(self, symbol_id):
        res = self.send_request(
            "get", settings.NAV_DATA_ENDPOINT_TEMPLATE.format(symbol_id=symbol_id)
        )
        if value := res.get("Value", None):
            return value

    def get_trades(self):
        res = self.send_request("get", settings.GET_TRADES_ENDPOINT)
        if res.get("IsSuccessfull", False):
            return res.get("Data")

    def create_order(self, symbol: str, count: int, price: int, is_buy=True):
        data = {
            "IsSymbolCautionAgreement": False,
            "CautionAgreementSelected": False,
            "IsSymbolSepahAgreement": False,
            "SepahAgreementSelected": False,
            "orderCount": count,
            "orderPrice": price,
            "FinancialProviderId": 1,
            "minimumQuantity": 0,
            "maxShow": 0,
            "orderId": 0,
            "isin": symbol.upper(),
            "orderSide": 65 if is_buy else 86,
            "orderValidity": 74,
            "orderValiditydate": None,
            "shortSellIsEnabled": False,
            "shortSellIncentivePercent": 0,
        }
        res = self.send_request("post", settings.CREATE_ORDER_ENDPOINT, json=data)
        if res.get("IsSuccessfull", False):
            return True
        raise Exception(
            res.get("MessageDesc", f"Order create failed! {symbol},{count},{price}")
        )

    def edit_order(
        self, order_id: int, symbol: str, count: int, price: int, is_buy=True
    ):
        data = {
            "orderCount": count,
            "orderPrice": price,
            "FinancialProviderId": 1,
            "minimumQuantity": 0,
            "maxShow": 0,
            "orderId": order_id,
            "isin": symbol,
            "orderSide": 65 if is_buy else 86,
            "orderValidity": 74,
            "orderValiditydate": None,
            "shortSellIsEnabled": False,
            "shortSellIncentivePercent": 0,
        }

        res = self.send_request("post", settings.EDIT_ORDER_ENDPOINT, json=data)
        if res.get("IsSuccessfull", False):
            return True
        raise Exception(
            res.get("MessageDesc", f"Order edit failed! {symbol},{count},{price}")
        )

    def remaining_assets(
        self,
        symbol: str,
    ):
        params = {"isin": symbol.upper()}

        res = self.send_request("get", settings.REMAINING_ASSET_ENDPOINT, params=params)
        if res.get("IsSuccessfull", False):
            return res.get("Data")
            # template:
            # [
            #     {
            #         "symbol": "اهرم",
            #         "nsccode": "IRT1AHRM0001",
            #         "symbolid": 0,
            #         "lasttradeprice": 0,
            #         "time": "09:37:56",
            #         "dtime": "1403/11/13",
            #         "orderprice": 25470.000000000,
            #         "customerid": 220703,
            #         "ProviderName": "TBRFinancialDataProvider",
            #         "Providerid": 1,
            #         "orderid": "3025020120015621",
            #         "ordervl": "Day",
            #         "ordervlFa": "روز",
            #         "ordervlid": 74,
            #         "gtdate": null,
            #         "gtdateMiladi": null,
            #         "orderside": "فروش",
            #         "ordersideid": 86,
            #         "qunatity": 200,
            #         "ExpectedQuantity": 200,
            #         "excuted": 0,
            #         "status": "ثبت در سیستم معاملات ",
            #         "visible": 1,
            #         "customername": null,
            #         "orderFrom": "OnlinePlus",
            #         "minimumQuantity": 0,
            #         "maxShow": 0,
            #         "HostOrderId": 4030,
            #         "OrderEntryDate": "20250201",
            #         "orderDateTime": null,
            #         "state": "onboard",
            #         "errorcode": null,
            #         "CSize": 0
            #     }
            # ]

        return None

    def delete_order(
        self,
        order_id: int,
    ):
        data = [str(order_id)]

        res = self.send_request("post", settings.DELETE_ORDER_ENDPOINT, json=data)
        if res.get("IsSuccessfull", False):
            if res_data := res.get("Data", {}):
                if res_data.get("SuccessCancel"):
                    return True
            return True
        raise Exception(res.get("MessageDesc", f"Order delete failed! {order_id}"))

    def price_ohlcv(
        self,
        symbol: str,
        resolution: str,
        time_from: datetime.datetime,
        time_to: datetime.datetime,
    ):
        params = {
            "symbol": symbol.upper(),
            "resolution": resolution,
            "from": int(time_from.timestamp()),
            "to": int(time_to.timestamp()),
        }

        res = self.send_request("get", settings.PRICE_OHLC_ENDPOINT, params=params)
        all_data = []
        if res.get("s", "ok"):
            for d in zip(
                res.get("t", []),
                res.get("o", []),
                res.get("h", []),
                res.get("l", []),
                res.get("c", []),
                res.get("v", []),
            ):
                data_time = datetime.datetime.fromtimestamp(float(d.pop(0)))
                all_data.append([data_time, *d])
            return all_data

        raise Exception(res.get("s", f"Price ohlc failed!"))

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
        endpoint,
        json=None,
        data=None,
        files=None,
        params=None,
        headers=None,
    ):
        res = self.sess.request(
            method, endpoint, params, data, headers, files=files, json=json
        )
        res = self.handle_response(res)
        return res
