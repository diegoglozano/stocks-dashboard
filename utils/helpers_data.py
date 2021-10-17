import pandas as pd
import streamlit as st
import yfinance as yf


@st.cache
def get_stock_prices(
    ticket: str,
    min_date,
    max_date
) -> pd.DataFrame:
    ticket = yf.Ticker(ticket)
    hist = (
        ticket
        .history(period='max')
        .reset_index()
    )
    return hist.loc[
        hist['Date'].between(str(min_date), str(max_date))
    ]