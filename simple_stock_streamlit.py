import yfinance as yf
import streamlit as st
import pandas as pd

st.header('Simple Stock Price App')
st.subheader('Shown are the stock closing price and volume of TJX Companies Inc.')

#define ticker symbol
tickerSymbol =  'TJX'

#get data
tickerData = yf.Ticker(tickerSymbol)

#get historical prices 
tickerDf = tickerData.history(period='1d', start = '2022-1-1', end = '2023-1-1')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)