# visualizing stock prices in real time

import pandas as pd
import pandas_datareader.data as daWeb
import matplotlib.pyplot as plot
import datetime
from datetime import date, timedelta
today = date.today()

dOne = today.strftime("%Y/%m/%d")
end_date = dOne
dTwo = date.today() - timedelta(days=360)
dTwo = dTwo.strftime("%Y/%m/%d")
start_date = dTwo

import streamlit as srt
srt.title("Stock Price Data, Brought to you by Nels2")
find = srt.text_input("Enter any company to search for >>: ")
data = daWeb.DataReader(name=find, data_source='yahoo', start=start_date, end=end_date)
fig, ax = plot.subplots()
ax = data["Close"].plot(figsize=(12, 8), title=find+"Stock Prices", fontsize=20, label="Close Price")
plot.legend()
plot.grid()
srt.pyplot(fig)
