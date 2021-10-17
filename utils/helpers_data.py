import pandas as pd
import streamlit as st
import yfinance as yf

from typing import Tuple, Dict

from utils.constants import TICKET_ATTRIBUTES

@st.cache
def get_stock_prices(
    ticket: str,
    min_date,
    max_date
) -> Tuple[pd.DataFrame, Dict[str, str]]:
    ticket = yf.Ticker(ticket)
    hist = (
        ticket
        .history(period='max')
        .reset_index()
    )

    info = {
        key: value
        for key, value in ticket.info.items()
        if key in TICKET_ATTRIBUTES
    }

    return (
        hist.loc[
            hist['Date'].between(str(min_date), str(max_date))
        ],
        info
    )