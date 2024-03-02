# from pybit.unified_trading import HTTP
# import json

# symbol = 'BTCUSDT'
# symbol = 'ARBUSDT'

# # Создание экземпляра класса PyBit с вашими данными API
# session = HTTP(
#     testnet=False,
#     api_key=api_key,
#     api_secret=api_secret,
# )

# def get_precisions(symbol):
#     try:
#         symbol_info = session.get_instruments_info(
#             category='linear',
#             symbol=symbol
#         )['result']['list'][0]
#         with open("info.json", "w") as f:
#             json.dump(symbol_info, f, indent=4)
#         # price = resp['priceFilter']['tickSize']
#         # if '.' in price:
#         #     price = len(price.split('.')[1])
#         # else:
#         #     price = 0
#         # qty = resp['lotSizeFilter']['qtyStep']
#         # if '.' in qty:
#         #     qty = len(qty.split('.')[1])
#         # else:
#         #     qty = 0

#         # return price, qty
#     except Exception as err:
#         print(err)

# print(get_precisions(symbol))

