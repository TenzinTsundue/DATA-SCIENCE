# Simple Stock Price

import yfinance as yf
import streamlit as st
import pandas as pd

# you can write in markdown
st.write("""
# Simple stock Price App

Show are the stock closing price and volume of Google!

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2021-5-23')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)