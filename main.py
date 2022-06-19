
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import numpy as np
import data as dt
import functions as fn

# -- 1) // Lectura de datos // -- #
ob_data = dt.order_books('files/orderbooks_05jul21.json')
pt_data = dt.public_trades('files/btcusdt_binance.csv')


# -- 2) // Obtener los mid price de los precios de ordenes
ob_metrics = fn.order_book_metrics(ob_data)
mid_prices = ob_metrics['Mid_Price']

# -- 3) // Obtener la diferencia de los precios 
delta_p = [mid_prices[i+1] - mid_prices[i] for i in np.arange(0,len(mid_prices)-1)]
delta2_p = np.diff(mid_prices)

delta_p[89]
delta2_p[89]

# -- 4) // Obtener ask y bid teoricos
var_cov_matrix = np.cov(delta_p[1:len(delta_p)-1],delta_p[2:])[0] # Matriz de varianzas covarianzas

cov = var_cov_matrix[1]
var = var_cov_matrix[0]

C = np.sqrt(-cov)
S = 2*C
# ob_metrics['Spread']

ask_teorico = [i+C for i in mid_prices]
bid_teorico = [i-C for i in mid_prices]

# -- 5) // Obtener ask y bid observados
ob_ts = list(ob_data.keys())
ask_observado = [ob_data[ob_ts[i]]['ask'][0]  for i in range(len(ob_ts))]
ask_observado = [ob_data[ob_ts[i]]['bid'][0]  for i in range(len(ob_ts))]

# Gráficas
