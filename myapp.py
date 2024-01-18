import yfinance as yf
import streamlit as st

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

    # Check if the data frame is empty
    if tickerDf.empty:
        st.write("No data available for the specified date range.")
    else:
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

except Exception as e:
    # Handle other generic exceptions
    st.error("An error occurred: " + str(e))
    st.write("Please check your internet connection, API parameters, or if the API service is available.")
