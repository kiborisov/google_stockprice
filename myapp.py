import yfinance as yf
import streamlit as st
import json

# Write the header of your Streamlit app
st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!
""")

# Define the ticker symbol for Google
tickerSymbol = 'GOOGL'

try:
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

    # Display the closing price
    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)

    # Display the volume price
    st.write("""
    ## Volume Price
    """)
    st.line_chart(tickerDf.Volume)

except json.JSONDecodeError as e:
    # Handle JSON decode errors
    st.error("Failed to decode JSON from response: " + str(e))
    st.write("Please check the API call or response format.")
except Exception as e:
    # Handle other generic exceptions
    st.error("An error occurred: " + str(e))
    st.write("Please check your internet connection or API parameters.")
