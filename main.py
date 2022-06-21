
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab 2 : High-Frequency Models                                                       -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: if722399                                                                      -- #
# -- license: GNU General Public License v3.0                                                  -- #
# -- repository: https://github.com/if722399/Laboratorio-2-MyST.git                                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import numpy as np
import data as dt
import functions as fn
import visualizations as vn

"""
Modelo 1. APT Model
"""
# -- 1) // Lectura de datos // -- #
ob_data = dt.order_books('files/orderbooks_05jul21.json')
pt_data = dt.public_trades('files/btcusdt_binance.csv')

# -- 2) // Obtener los mid price de los precios de ordenes
ob_metrics = fn.order_book_metrics(ob_data)
mid_prices = ob_metrics['Mid_Price']

# -- 3) // Obtener los weighted mid price de los precios de ordenes
weighted_mid_prices = ob_metrics['Weighted-Midprice (B)']

# -- 4) // Probar el modelo 1 (Martingalas)
mtg = fn.Martingala(ob_data,mid_prices)

# -- 5) // Gráfico

vn.Model1(mtg['Minute'], mtg['Martingala'], mtg['No Martingala'])




"""
Modelo 2. Roll Model
"""

# -- 1) // Obtener la diferencia de los precios 
delta_p = [mid_prices[i+1] - mid_prices[i] for i in np.arange(0,len(mid_prices)-1)]
delta2_p = np.diff(mid_prices)

delta_p[89]
delta2_p[89]

# -- 2) // Obtener ask y bid teoricos
var_cov_matrix = np.cov(delta_p[1:len(delta_p)-1],delta_p[2:])[0] # Matriz de varianzas covarianzas

cov = var_cov_matrix[1]
var = var_cov_matrix[0]

C = np.sqrt(-cov)
S = 2*C
# ob_metrics['Spread']

ask_teorico = [i+C for i in mid_prices]
bid_teorico = [i-C for i in mid_prices]

# -- 3) // Obtener ask y bid observados
ob_ts = list(ob_data.keys())
ask_observado = [ob_data[ob_ts[i]]['ask'][0]  for i in range(len(ob_ts))]
bid_observado = [ob_data[ob_ts[i]]['bid'][0]  for i in range(len(ob_ts))]


# -- 4) // Gráficas

vn.Model2_1() # Ask prices

vn.Model2_2() # Mid prices

