import time

from src import settings
from src.adapters.data_adapter import DataAdapter
from src.adapters.pishro_adapter import PishroAdapter

# Run the app
if __name__ == "__main__":
    data = DataAdapter()
    adapter = PishroAdapter(settings.USER_NAME, settings.PASSWORD)
    if not adapter.login():
        raise Exception("Credentials Error or Captcha Read failed")

    all_symbols = adapter.get_all_symbols()
    adapter.js_server_adapter.subscribe_stock_queue(['IRO1PTEH0001', 'IRO1BMLT0001'])
    print(1)
    time.sleep(2)
    print(2)
    adapter.js_server_adapter.subscribe_stock_queue(['IRO1TAMN0001'])
    time.sleep(5)

    adapter.js_server_adapter.stop_server()


    myvar = data.get("myvar")
    also_my_var = data.get_pickle("myvar")
