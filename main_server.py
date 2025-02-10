from sanic import Sanic
from sanic.request import Request
from sanic.response import json

from src import settings
from src.adapters.pishro_adapter import PishroAdapter

app = Sanic("MarketIndexApp")


@app.post("/market-index")
async def market_index(request: Request):
    # Get the JSON data from the request
    data: dict = request.json
    symbol = data["itemName"].replace("_lightrlc", "")
    day_of_event = data["updateValues"][7]
    percent_variation = data["updateValues"][6]
    index_changes = data["updateValues"][5]
    last_index_value = data["updateValues"][4]

    # Respond with a success message
    return json({"message": "Data received successfully!"})


@app.post("/stock")
async def stock(request: Request):
    # Get the JSON data from the request
    data: dict = request.json

    # Respond with a success message
    return json({"message": "Data received successfully!"})


@app.post("/stock-watch-list")
async def stock_watch_list(request: Request):
    # Get the JSON data from the request
    data: dict = request.json

    # Respond with a success message
    return json({"message": "Data received successfully!"})


@app.post("/stock-queue")
async def stock_queue(request: Request):
    # Get the JSON data from the request
    data: dict = request.json
    print(data)
    # symbol = data["itemName"].replace("_lightrlc", "")
    # best_buy_limit_price_1 = data["updateValues"][2]
    # best_sell_limit_price_1 = data["updateValues"][3]
    # best_buy_limit_quantity_1 = data["updateValues"][4]
    # best_sell_limit_quantity_1 = data["updateValues"][5]
    # number_of_orders_at_best_buy_1 = data["updateValues"][7]
    # best_buy_limit_price_2 = data["updateValues"][8]
    # best_sell_limit_price_2 = data["updateValues"][9]
    # best_buy_limit_quantity_2 = data["updateValues"][10]
    # best_sell_limit_quantity_2 = data["updateValues"][11]
    # number_of_orders_at_best_buy_2 = data["updateValues"][12]
    # best_buy_limit_price_3 = data["updateValues"][14]
    # best_sell_limit_price_3 = data["updateValues"][15]
    # best_buy_limit_quantity_3 = data["updateValues"][16]
    # best_sell_limit_quantity_3 = data["updateValues"][17]
    # number_of_orders_at_best_buy_3 = data["updateValues"][18]
    # best_buy_limit_price_4 = data["updateValues"][20]
    # best_sell_limit_price_4 = data["updateValues"][21]
    # best_buy_limit_quantity_4 = data["updateValues"][22]
    # best_sell_limit_quantity_4 = data["updateValues"][23]
    # number_of_orders_at_best_buy_4 = data["updateValues"][24]
    # best_buy_limit_price_5 = data["updateValues"][26]
    # best_sell_limit_price_5 = data["updateValues"][27]
    # best_buy_limit_quantity_5 = data["updateValues"][28]
    # best_sell_limit_quantity_5 = data["updateValues"][29]
    # number_of_orders_at_best_buy_5 = data["updateValues"][30]

    # TODO add logics
    # Respond with a success message
    return json({"message": "Data received successfully!"})


@app.post("/market-depth")
async def market_depth(request: Request):
    # Get the JSON data from the request
    data: dict = request.json

    # Respond with a success message
    return json({"message": "Data received successfully!"})


# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
