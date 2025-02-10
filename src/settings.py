import os

USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
GET_CAPTCHA_ENDPOINT = os.getenv("GET_CAPTCHA_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/Authenticate/GetCaptchaImage/Captcha")
LOGIN_ENDPOINT = os.getenv("LOGIN_ENDPOINT", "https://api.pishrobroker.ir/Web/V2/Authenticate/Login")
PORTFOLIO_ENDPOINT = os.getenv("PORTFOLIO_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/DailyPortfolio/Get/DailyPortfolio?symbolIsin=")
ALL_SYMBOLS_ENDPOINT = os.getenv("ALL_SYMBOLS_ENDPOINT", "https://core.tadbirrlc.com/StocksHandler?{%22Type%22:%22allSymbols%22,%22la%22:%22fa%22}&jsoncallback=")
ALL_SECTORS_ENDPOINT = os.getenv("ALL_SECTORS_ENDPOINT", "https://core.tadbirrlc.com//StocksHandler?%7B%22Type%22:%22sectors%22,%22la%22:%22fa%22%7D&jsoncallback=")
NAV_DATA_ENDPOINT_TEMPLATE = os.getenv("NAV_DATA_ENDPOINT_TEMPLATE", 'https://core.tadbirrlc.com/StockFutureInfoHandler?{"Type":"etf","la":"fa","nscCode":"{symbol_id}"}&jsoncallback=')
CREATE_ORDER_ENDPOINT =  os.getenv("CREATE_ORDER_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/Order/Post")
EDIT_ORDER_ENDPOINT =  os.getenv("EDIT_ORDER_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/Order/PUT")
DELETE_ORDER_ENDPOINT =  os.getenv("DELETE_ORDER_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/Order/Delete")
OPEN_ORDERS_ENDPOINT =  os.getenv("OPEN_ORDERS_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/Order/GetOpenOrder/OpenOrder")
REMAINING_ASSET_ENDPOINT =  os.getenv("REMAINING_ASSET_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/DailyPortfolio/GetRemainAsset/GetRemainAsset")
PRICE_OHLC_ENDPOINT =  os.getenv("PRICE_OHLC_ENDPOINT", "https://api.pishrobroker.ir/Web/V1/DailyPortfolio/GetRemainAsset/GetRemainAsset")
GET_TRADES_ENDPOINT = os.getenv("GET_TRADES_ENDPOINT", "https://rlcchartapi.tadbirrlc.ir/ChartData/history")
LIGHTSTREAMER_ENDPOINT = os.getenv("LIGHTSTREAMER_ENDPOINT")
BROKER_ID = os.getenv("BROKER_ID", "181")
JS_SERVER_FILE_PATH = "src/js/src/main.js"
JS_SERVER_PORT = 3000
