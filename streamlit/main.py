import streamlit as st
import pandas as pd
import os

from utils.binance_client import BinanceClient
from utils.logger import get_logger
from utils.visualization import plot_klines

logger = get_logger("main")
# handler = Handler()

DEFAULT_KEY_TO_VALUES = {"target": "BTCUSDT", "duration": 24, "interval": "5m"}


def initialize_session_state(keys_to_values):
    for key, value in keys_to_values.items():
        if key not in st.session_state:
            st.session_state[key] = value


def main():
    binance_api = BinanceClient(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_API_SECRET"))
    st.text_input("Coin", "BTCUSDT", key="target")
    st.text_input("Duration", 24, key="duraton")
    st.text_input("Interval", "5m", key="interval")

    def on_click():
        klines = binance_api.get_klines(
            symbol=st.session_state.target,
            start_str=(pd.Timestamp.now() - pd.Timedelta(hours=st.session_state.duration)).strftime(
                "%Y-%m-%d' %H:%M:%S"
            ),
            interval=st.session_state.interval,
        )
        fig = plot_klines(klines, st.session_state.target)
        st.pyplot(fig)

    st.button("Start", on_click=on_click)


if __name__ == "__main__":
    initialize_session_state(DEFAULT_KEY_TO_VALUES)
    main()
