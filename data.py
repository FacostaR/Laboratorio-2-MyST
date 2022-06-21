
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab 2 : High-Frequency Models                                                   -- #
# -- script: data.py : python script for data collection                                                  -- #
# -- author: if722399                                                                    -- #
# -- license: GNU General Public License v3.0                                              -- #
# -- repository: https://github.com/if722399/Laboratorio-2-MyST.git                                                          -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""


"""
# -----------------------  Funciones para descargar los datos:  ----------------------- #
"""

"""
1) Descargar order books:
"""
# Importar Librerias
import pandas as pd
import json 

def order_books(file_name):
    # Opening JSON file
    f = open(file_name)
    print(f)

    # Returns JSON object as a dictionary
    orderbooks_data = json.load(f)
    ob_data = orderbooks_data['bitfinex']

    # Drop Keys with none values
    ob_data = {i_key: i_value for i_key,i_value in ob_data.items() if i_value is not None}

    # Convert to DataFrame and rearange columns
    ob_data = {i_ob: pd.DataFrame(ob_data[i_ob])[['bid_size', 'bid', 'ask', 'ask_size']]
            if ob_data[i_ob] is not None else None for i_ob in list(ob_data.keys())}
    return ob_data

"""
2) Public Trades:
"""
def public_trades(file_name):
    pt_data = pd.read_csv(file_name, header=0)
    pt_data.index = pd.to_datetime(pt_data['timestamp'])
    return pt_data



# Prueba
ob_data = order_books('files/orderbooks_05jul21.json')
pt_data = public_trades('files/btcusdt_binance.csv')

