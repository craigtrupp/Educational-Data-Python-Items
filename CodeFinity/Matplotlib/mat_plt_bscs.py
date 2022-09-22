#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 09:34:00 2022

@author: craigrupp
"""

# Building Block
# =============================================================================
# The basic concept of building plots in matplotlib is using two objects: 
# Figure as a space for building your graph and Axes - an area where points can be specified (usually in terms of x-y coordinates, but also in a 3D plot, for example, and so on).
# To create both Figure and Axes you can use .subplots() function from matplotlib.pyplot using multiple assignment 
# (we need create two variables: for Figure and Axes objects)
# =============================================================================

# =============================================================================
# # Standard Emplty plot 
# =============================================================================

# Import the libraries for usage
import matplotlib.pyplot as plt
import pandas as pd

# Create Figure and Axes objects
fig, ax = plt.subplots()

# Initialize an empty plot
ax.plot()

# Display the plot
plt.show()


# =============================================================================
# Build a line chart representing the level of CO2 emissions (metric tonnes of CO2 per person). for USA
# =============================================================================

# Load the data
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/ed80401e-2684-4bc4-a077-99d13a386ac7/co2.csv', index_col = 0)
print(data.head())
# index is set to our flat files first columns, each country only included once
print(data.index.value_counts())

# Filter the data for USA Data
usa = data.loc["United States"]
print(usa, type(usa))
print(data.loc['United States', :])

# Create Figure and Axes objects 
fig, ax = plt.subplots()

# Initialize the plot for USA Series filtered above
ax.plot(usa.index.astype('int'), usa.values)

# Display the plot
plt.show()


# =============================================================================
# Multiple Line Instances - Legend Usage
# =============================================================================
can = data.loc['Canada']
print(len(can), len(usa))

# New Axes Objects
fig_2, ax_2 = plt.subplots()

# Include label for legend
ax_2.plot(usa.index.astype('int'), usa.values, label='USA')
ax_2.plot(can.index.astype(int), can.values, label='CAN')
ax_2.legend()


# Add legend, labels, and title
ax_2.set_xlabel('Year')
ax_2.set_ylabel('CO2 emission per person (metric tonnes)')
plt.title('CO2 emissions (tonnes per person) in the USA and Canada')
plt.legend()
plt.show()    


# =============================================================================
# More Customizations to Plot Calls (made on axes object)
# {Color : Set the color of the line (and points), Line style : Sets the style for the line (ex : dash or dotted), Points style (marker) : Sets the marker type (for example, circle or triangle points)}
# : https://matplotlib.org/stable/gallery/color/named_colors.html https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
# =============================================================================

fig_3, ax_3 = plt.subplots()

# Australia, France, South Africa
data_3 = data.loc[['Australia', 'France', 'South Africa']]

# Plot Each dataframe row
ax_3.plot(data_3.columns.astype(int), data_3.loc['Australia'], label='Australia', color='yellow', marker='v', linestyle='dashed')
ax_3.plot(data_3.columns.astype(int), data_3.loc['France'], label='France', color='blue', marker='8', linestyle='dotted')
ax_3.plot(data_3.columns.astype(int), data_3.loc['South Africa'], label='South Africa', color='green', marker='d', linestyle='dashdot')

# Set labels and legend
ax_3.set_xlabel('Year')
ax_3.set_ylabel('CO2 emission per person (metric tonnes)')
plt.title('CO2 emissions (tonnes per person)') 
plt.legend()
plt.show()
    


# New Data Set
# =============================================================================
# Given dataframe us_cities_weather containing the weather data for the US cities (average temperature per month from 1961 - 1990 in Fahrenheit). 
# You need to display the monthly average temperature for three cities: San Francisco, Denver, and Miami. 
# =============================================================================

# Load the data
us_cities_weather = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/ed80401e-2684-4bc4-a077-99d13a386ac7/US+cities+weather+data.csv', index_col = 0)
print(us_cities_weather.head())

# Subset Cities
us_cities = us_cities_weather.loc[['San Francisco', 'Denver', 'Miami']]
print(us_cities.head())
print(us_cities.loc['Denver'])

# Create Figure and Axes objects
fig_4, ax_4 = plt.subplots()

# Save data for three cities
sf = us_cities.loc["San Francisco"]
dv = us_cities.loc["Denver"]
mm = us_cities.loc["Miami"]

# Initialize the plot
ax_4.plot(sf["Month"], sf["Temperature"], label = 'San Francisco', color = 'r', 
        marker = "s", linestyle = "dotted")
ax_4.plot(dv["Month"], dv["Temperature"], label = 'Denver', color = 'b',
        marker = "^", linestyle = "dashed")
ax_4.plot(mm["Month"], mm["Temperature"], label = 'Miami', color = 'darkorange',
        marker = "o", linestyle = "dashdot")

# Set custom labels on axis
ax_4.set_xlabel("Month")
ax_4.set_ylabel("Average Temperature (Fahrenheit)")

# Add plot title and display the plot
plt.title("Moving Monthly Temperature Avg 1961-1990")
plt.legend()
plt.show()

 
    
    
    
    