
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab 2 : High-Frequency Models                                                        -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: if722399                                                                   -- #
# -- license: GNU General Public License v3.0                                                  -- #
# -- repository: https://github.com/if722399/Laboratorio-2-MyST.git                                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""
            Gráfico del modelo 1
"""

def Model1(minutes,Martingala,No_martingala):
        # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])


    # Add traces
    fig.add_trace(
    go.Bar(x=minutes, y=Martingala, name="Martingala"),
    secondary_y=True,
    )

    fig.add_trace(
    go.Bar(x=minutes, y=No_martingala, name="No_martingala"),
    secondary_y=True,
    )

     # Add figure title
    fig.update_layout(
        title_text="Modelo 1: Martingalas"
    )
    
    # Set x-axis title
    fig.update_xaxes(title_text="Minutos")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b># de apariciones</b> <br> Martingalas // No Martingalas", secondary_y=False)

    #fig.update_layout(legend_orientation='h', xaxis=dict(ticktext=list(data_pt['timestamp'])[0:499]) )

    fig.show()



"""
            Gráficos del modelo 2
"""

def Model2_1():
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])


    # Add traces
    fig.add_trace(
        go.Scatter(x=mn.ob_ts[1:], y= mn.ask_teorico, name="Ask Teorico"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=mn.ob_ts[1:], y= mn.ask_observado, name="Ask Observado"),
        secondary_y=False,
    )


    # Add figure title
    fig.update_layout(
        title_text="Ask teoricos vs Ask observados"
    )
    
    # Set x-axis title
    fig.update_xaxes(title_text="Timestamp")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Prices</b> <br> BTC/USDT", secondary_y=False)

    #fig.update_layout(legend_orientation='h', xaxis=dict(ticktext=list(data_pt['timestamp'])[0:499]) )

    fig.show()

def Model2_2():
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])


    # Add traces
    fig.add_trace(
        go.Scatter(x=mn.ob_ts[1:], y= mn.bid_teorico, name="Bid Teorico"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=mn.ob_ts[1:], y= mn.bid_observado, name="Bid Observado"),
        secondary_y=False,
    )


    # Add figure title
    fig.update_layout(
        title_text="Bid teoricos vs Bid observados"
    )
    
    # Set x-axis title
    fig.update_xaxes(title_text="Timestamp")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Prices</b> <br> BTC/USDT", secondary_y=False)

    #fig.update_layout(legend_orientation='h', xaxis=dict(ticktext=list(data_pt['timestamp'])[0:499]) )

    fig.show()



    # Model2_1()
    # Model2_2()