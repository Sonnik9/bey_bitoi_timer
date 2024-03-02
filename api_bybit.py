import hmac
import hashlib
import requests
import time
from decimal import Decimal
from init_params import PARAMS

base_url = "https://api.bybit.com"

class BYBIT_API(PARAMS):
    def __init__(self):
        super().__init__()
    # POST
    def hashing(self, query_string):
        return hmac.new(self.api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    def place_market_order(self, symbol, side, qnt):
        try:
            base_url = "https://api.bybit.com/v5/order/create"
            timestamp = str(int(time.time() * 1000))
            data = '{' + f'"symbol": "{symbol}", "side": "{side}", "orderType": "Market", "qty": "{qnt}", "category": "spot"' + '}'
            sign = self.hashing(timestamp + self.api_key + '5000' + data)
            headers = {
                'X-BAPI-API-KEY': self.api_key,
                'X-BAPI-TIMESTAMP': timestamp,
                'X-BAPI-SIGN': sign,  
                'X-BAPI-RECV-WINDOW': '5000',            
            }            
            return requests.post(base_url, headers=headers, data=data)            
        except Exception as e:
            print(f"An error occurred: {e}")
            return

    # GET
    def get_exchange_info(self, symbol):
        endpoint = "/v2/public/symbols"
        url = f"{base_url}{endpoint}"
        try:
            response = requests.get(url)
            data = response.json()            
            symbol_info = next((item for item in data['result'] if item['name'] == symbol), None)
            return symbol_info
        except Exception as ex:
            print(ex)
            return None

    def get_current_price(self, symbol):
        endpoint = "/v2/public/tickers"
        url = f"{base_url}{endpoint}?symbol={symbol}"
        try:
            response = requests.get(url)
            data = response.json()            
            return float(data['result'][0]['last_price'])
        except Exception as ex:
            print(ex)
            return None
       
    # # //utils//////////////////////////////////////////////////////////////////////////
    # def usdt_to_qnt_converter(self, symbol): 
    #     try:
    #         symbol_info = self.get_exchange_info(symbol)
    #         qtyStep = str(float(symbol_info['lot_size_filter']['min_trading_qty']))
    #         quantity_precision = Decimal(qtyStep).normalize().to_eng_string()        
    #         quantity_precision = len(quantity_precision.split('.')[1])     
    #         return quantity_precision
    #     except Exception as ex:
    #         print(ex)
    #         return None, None
        
    # def usdt_to_qnt_converter(self, symbol, depo): 
    #     try:
    #         symbol_info = self.get_exchange_info(symbol)
    #         min_qty = float(symbol_info['lot_size_filter']['min_trading_qty'])
    #         max_qty = float(symbol_info['lot_size_filter']['max_trading_qty'])
    #         qtyStep = str(float(symbol_info['lot_size_filter']['min_trading_qty']))
    #         quantity_precision = Decimal(qtyStep).normalize().to_eng_string()        
    #         quantity_precision = len(quantity_precision.split('.')[1])           
    #         price = self.get_current_price(symbol)
    #         # print(price)
    #         qnt = round(depo / price, quantity_precision)
    #         if qnt <= min_qty:
    #             qnt = min_qty               
    #         elif qnt >= max_qty:
    #             qnt = max_qty        
    #         return qnt, quantity_precision
    #     except Exception as ex:
    #         print(ex)
    #         return None, None