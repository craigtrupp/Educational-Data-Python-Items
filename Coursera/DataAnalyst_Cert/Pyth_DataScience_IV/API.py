#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:49:17 2022

@author: craigrupp
"""

!pip install pycoingecko
!pip install plotly
!pip install mplfinance

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc


dict_={'a':[11,21,31],'b':[12,22,32]}

# Pandas API is communicated with when creating an instance (most commonly a DataFrame)
# =============================================================================
# # When you create a Pandas object with the Dataframe constructor in API lingo, this is an "instance". 
# # The data in the dictionary is passed along to the pandas API. You then use the dataframe to communicate with the API.
# =============================================================================
df=pd.DataFrame(dict_)
type(df)

# When you call the method head the dataframe communicates with the API displaying the first few rows of the dataframe.
df.head()


# Rest API - Representational State Transfer
# =============================================================================
# Rest API’s function by sending a request, the request is communicated via HTTP message. 
# The HTTP message usually contains a JSON file. This contains instructions for what operation we would like the service or resource to perform. 
# In a similar manner, API returns a response, via an HTTP message, this response is usually contained within a JSON.
# =============================================================================


# Lab
# =============================================================================
# CoinGecko API to create one of these candlestick graphs for Bitcoin. 
# We will use the API to get the price data for 30 days with 24 observation per day, 1 per hour. 
# We will find the max, min, open, and close price per day meaning we will have 30 candlesticks and use that to generate the candlestick graph. 
# Although we are using the CoinGecko API we will use a Python client/wrapper for the API called <a href=https://github.com/man-c/pycoingecko?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2022-01-01>PyCoinGecko. 
# PyCoinGecko will make performing the requests easy and it will deal with the enpoint targeting.
# =============================================================================

cg = CoinGeckoAPI()

# Data we're retrieving : get_coin_market_chart_by_id is looking for three arguments to return data back from the API
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
type(bitcoin_data)
print(bitcoin_data) # wow that's a giant dictionary!
print(bitcoin_data.keys())

# The response we get is in the form of a JSON which includes the price, market caps, and total volumes along with timestamps for each observation. 
# We are focused on the prices so we will select that data.
bitcoin_price_data = bitcoin_data['prices']

bitcoin_price_data[0:5]

# Let's transform the dictionary into a dataframe
bc_price_data = pd.DataFrame(bitcoin_price_data)
print(bc_price_data.head())

# The List pairs hold a timestamp value and closing price, so let's rename our default index columns
bc_price_data.rename(columns = {0:'Timestamp', 1:'Price'}, inplace=True)
bc_price_data.head()

# Now that we have the DataFrame we will convert the timestamp to datetime and save it as a column called Date. 
# We will map our unix_to_datetime to each timestamp and convert it to a readable datetime
bc_price_data['date'] = bc_price_data['Timestamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))
print(bc_price_data.head())

# Various rows per date, let's get some Agg Stats from it : min, max, open, and close for the candlesticks.
# Notice how Price is included in the agg outlay so as to pass to figure created below
cd_data = bc_price_data.groupby('date').agg({"Price": ['min', 'max', 'first', 'last']}).reset_index()
print(cd_data)

# Another Way to do the above (a bit different than I do but how the course detailed)
candlestick_data = bc_price_data.groupby(bc_price_data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})
print(candlestick_data)



# Display Candles with Agg Data from Cd_data holding the grouped by stats for each day
# Set 
fig = go.Figure(data=[go.Candlestick(x=cd_data['date'],
                open=cd_data['Price']['first'], 
                high=cd_data['Price']['max'],
                low=cd_data['Price']['min'], 
                close=cd_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()































