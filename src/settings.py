import os

USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
GET_CAPTCHA_ENDPOINT = os.getenv("GET_CAPTCHA_ENDPOINT")
LOGIN_ENDPOINT = os.getenv("LOGIN_ENDPOINT")
PORTFOLIO_ENDPOINT = os.getenv("PORTFOLIO_ENDPOINT")
ALL_SYMBOLS_ENDPOINT = os.getenv("ALL_SYMBOLS_ENDPOINT")
ALL_SECTORS_ENDPOINT = os.getenv("ALL_SECTORS_ENDPOINT")
NAV_DATA_ENDPOINT_TEMPLATE = os.getenv("NAV_DATA_ENDPOINT_TEMPLATE")
CREATE_ORDER_ENDPOINT =  os.getenv("CREATE_ORDER_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/Order/Post")
EDIT_ORDER_ENDPOINT =  os.getenv("EDIT_ORDER_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/Order/PUT")
DELETE_ORDER_ENDPOINT =  os.getenv("DELETE_ORDER_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/Order/Delete")
OPEN_ORDERS_ENDPOINT =  os.getenv("OPEN_ORDERS_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/Order/GetOpenOrder/OpenOrder")
REMAINING_ASSET_ENDPOINT =  os.getenv("REMAINING_ASSET_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/DailyPortfolio/GetRemainAsset/GetRemainAsset")

GET_TRADES_ENDPOINT = os.getenv("GET_TRADES_ENDPOINT", "")

LIGHTSTREAMER_ENDPOINT = os.getenv("LIGHTSTREAMER_ENDPOINT")
BROKER_ID = os.getenv("BROKER_ID")
JS_SERVER_FILE_PATH = "js/src/main.js"
JS_SERVER_PORT = 3000

