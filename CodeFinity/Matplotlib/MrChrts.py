#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:52:59 2022

@author: craigrupp
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Given dataframe data with rainfall information for Indian cities/districts
# Load the data
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/ed80401e-2684-4bc4-a077-99d13a386ac7/rainfall+in+india.csv', index_col = 0)

print(data.head())
# Times City/Index appears
print(data.index.value_counts())
print(data.index.unique())

# =============================================================================
# # Bar Graph for city of Interest
# =============================================================================
# City of Interest : New Delhi (Grab all rows by simple loc for index value)
ND = data.loc['NEW DELHI']
print(ND, type(ND))

fig, ax = plt.subplots()

ax.bar(ND['Month'], ND['Rainfall'])
plt.show()


# =============================================================================
# Stacked Bar Charts
# =============================================================================
# =============================================================================
# Save data for NEW DELHI in new_delhi variable, and for MADURAI in madurai variable.
# Call .bar function twice: the first time to build new_delhi data 
# ('Month' column on the x-axis, 'Rainfall' column on the y-axis), and then to build data for madurai above (the same columns and order as for the new_delhi data). 
# Use New Delhi and Madurai as label parameters.
# Display the legend of the plot.
# =============================================================================

# ND variable already available 
Madurai = data.loc['MADURAI']
if len(Madurai) == len(ND):
    print("same amount of observed values to plt on same axes")

fig_2, ax_2 = plt.subplots()

ax_2.bar(ND['Month'], ND['Rainfall'], label='New Delhi')
# Set bottom parameter to preceding or bottom bar's y_value 
ax_2.bar(Madurai['Month'], Madurai['Rainfall'], label='Madurai', bottom=ND['Rainfall'])

plt.legend()
plt.show()



# =============================================================================
# Grouped Bar Charts
# =============================================================================
# =============================================================================
# Save data for MUMBAI CITY in the mumbai variable, and all unique values from the Month column in the months variable.
# Set width to 0.3.
# Set correct first argument according to the approach above. With the last .bar() function call display the mumbai data. Set label to 'Mumbai'.
# Set months as x ticks labels.
# =============================================================================
Mumbai = data.loc['MUMBAI CITY']
combined = data.loc[['NEW DELHI', 'MADURAI', 'MUMBAI CITY']]
print(combined)

# Filter to certain cities
Mumbai = data.loc["MUMBAI CITY"]
months = data["Month"].unique()

# Create numpy array and width
x = np.arange(len(months))
width = 0.3

# Create Axes and Figure objects
fig_3, ax_3 = plt.subplots()

# Initialize the bar chart
ax_3.bar(x - width, ND["Rainfall"], width, label = 'New Delhi')
ax_3.bar(x, Madurai["Rainfall"], width, label = 'Madurai')
ax_3.bar(x + width, Mumbai["Rainfall"], width, label = 'Mumbai')

# Set x ticks
ax_3.set_xticks(x, labels=months)
ax_3.set(xlabel='Months', ylabel='Average Rainfall', title='Average Yearly Rainfall')

# Rotate ticks
plt.xticks(rotation=45)

# Display the legend and the plot
plt.legend()
plt.show()



# =============================================================================
# Horizontal Bar Chart
# =============================================================================
# =============================================================================
# For the same dataframe data build a horizontal bar chart representing the average monthly rainfall level for New Delhi and Madurai. 
# Follow the next steps:
# 
# Extract data for NEW DELHI and MADURAI and save it in new_delhi and madurai variables respectively.
# Initialize horizontal bar charts, placing the madurai data to the right of new_delhi data ('Month' column as the first parameter, and 'Rainfall' as the second). 
# Set label to New Delhi and Madurai.
# =============================================================================

fig_4, ax_4 = plt.subplots()

g = ax_4.barh(ND['Month'], ND['Rainfall'], label='New Delhi', height=0.4)
s = ax_4.barh(Madurai['Month'], Madurai['Rainfall'], left=ND['Rainfall'], label='Madurai', height=0.4)

ax_4.bar_label(g, label_type='edge', padding=-6.5)
ax_4.bar_label(s, label_type='edge', padding=5)

plt.legend()
plt.show()


# =============================================================================
# # More Customization
# =============================================================================

# Filter to certain cities
new_delhi = data.loc["NEW DELHI"]
mumbai = data.loc["MUMBAI CITY"]
months = data["Month"].unique()

# Create numpy array and width
x = np.arange(len(months))
width = 0.3

# Create Axes and Figure objects
fig_5, ax_5 = plt.subplots()

# Initialize the bar chart
bar1 = ax_5.barh(new_delhi["Month"], new_delhi["Rainfall"], label = 'New Delhi')

bar2 = ax_5.barh(mumbai["Month"], mumbai["Rainfall"], label = 'Mumbai', left = new_delhi["Rainfall"])

# Set labels, and title
ax_5.set(xlabel = "Rainfall (mm)", title = 'Average rainfall level in Indian cities', ylabel = 'Month', xlim = (0, 380))

# Add labels above bars
ax_5.bar_label(bar1, padding = -5)
ax_5.bar_label(bar2, padding = 5)

# Display the legend and the plot
plt.legend()
plt.show()



# =============================================================================
# Histograms
# Histograms, unlike bar charts, represent the frequency the values are met : COUNT(*) of a particular partition
# =============================================================================
# =============================================================================
# Create Figure and Axes objects assigned to fig, ax variables.
# From the data dataframe extract the rainfall level data for only October month (OCT value in the Month column) and save it in the october variable.
# Initialize the histogram for 'Rainfall' column from the extracted data, and set width to 40.
# Display the plot.
# =============================================================================

fig_6, ax_6 = plt.subplots()
months = data['Month'].unique()
print(months)

# Get all Rows with Oct Month column
october = data.loc[data['Month'] == 'OCT']
print(october)

# Histogram with Rainfall rows Octover Only (641 Indian Cities measured)
# To set a custom number of 'diapasons' use bins argument, and to focus on specific range use range (possible value is tuple (min, max)
# Max value is around 500 but what appears to be a bit of an outlier, let's narrow the histogram tail
ax_6.hist(october['Rainfall'], width=10, bins=20, range=(october['Rainfall'].min(), 300))
ax_6.set(ylabel='Total Cities Count', xlabel='Average Rainfall', title='October total Rain Distribution')

plt.show()


# =============================================================================
# Overlapping Histograms
# =============================================================================
# =============================================================================
# Extract the data for March month (MAR value in Month column).
# Initialize two histograms: the first one for the 'Rainfall' column from the october variable, 
# the second one for the 'Rainfall' column from the march variable. Set the width to 40, alpha to 0.5, and label to 'October' and 'March' respectively.
# Add a legend to the plot.
# =============================================================================

fig_7, ax_7 = plt.subplots()

march = data.loc[data['Month'] == 'MAR']
print(march)

ax_7.hist(october['Rainfall'], width=20, bins=15, range=(october['Rainfall'].min(), 350), alpha=0.5, label='October')
ax_7.hist(march['Rainfall'], width=20, bins=15, range=(march['Rainfall'].min(), 350), alpha=0.5, label='March')
ax_7.set(ylabel='Total Cities Count', xlabel='Average Rainfall', title='Spring/Fall Distribution')

plt.legend()
plt.show()





