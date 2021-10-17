from datetime import date, datetime
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

from datetime import datetime

from plotly.subplots import make_subplots

from utils.helpers_data import (
    get_stock_prices
)
from utils.constants import MIN_DATE, MAX_DATE, HEIGHT, WIDTH


ticket_choice = st.sidebar.text_input('Choose a stock')
min_date_choice = st.sidebar.date_input(
    label='Min date',
    value=MIN_DATE,
    min_value=MIN_DATE,
    max_value=MAX_DATE
)
max_date_choice = st.sidebar.date_input(
    label='Max date',
    value=MAX_DATE,
    min_value=MIN_DATE,
    max_value=MAX_DATE
)

try:
    prices, info = get_stock_prices(
        ticket_choice,
        min_date_choice,
        max_date_choice
    )

    if not prices.empty:
        st.title(info['shortName'])
        st.markdown(f'[{info["shortName"]}]({info["website"]})')
        st.write(info['longBusinessSummary'])
        fig = make_subplots(
            rows=2, 
            cols=1, 
            shared_xaxes=True, 
            vertical_spacing=0.03, 
            subplot_titles=('OHLC', 'Volume'), 
            row_width=[0.2, 0.7],
            
        )

        fig.add_trace(
            go.Candlestick(
                x=prices.index,
                open=prices['Open'],
                high=prices['High'],
                low=prices['Low'],
                close=prices['Close'],
                name=f'{ticket_choice}'
            )
        )
        fig.add_trace(
            go.Bar(
                x=prices.index, 
                y=prices['Volume'], 
                showlegend=False
            ), 
            row=2, 
            col=1
        )
        fig.update_layout(
            width=WIDTH,
            height=HEIGHT
        )
        st.plotly_chart(fig)

    else:
        if ticket_choice != '':
            st.write(f'Cannot find {ticket_choice}')

except Exception as e:
    st.write(e)
