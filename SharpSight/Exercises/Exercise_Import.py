#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:12:42 2022

@author: craigrupp
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


country_data = pd.read_csv('https://learn.sharpsightlabs.com/wp-content/datasets/pdm/country_data.csv', index_col = 'country_code')
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
sales_data = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/sales_data.csv')
emp_fst_nm = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/emp_fst_nm.csv')
emp_lst_nm = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/emp_lst_nm.csv')
bank = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')
revenue_tidy = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/revenue_tidy.csv')
revenue_wide = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/revenue_wide.csv')
revenue_world_Q3Q4 = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/revenue_world_Q3Q4.csv')
stocks = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/stocks.csv')
stocks.date = pd.to_datetime(stocks.date)
aapl_stock = stocks.query("stock == 'aapl'")
heatmap_data = pd.read_csv("https://learn.sharpsightlabs.com/datasets/pdm/heatmap_data.csv", index_col = 'education')

parking_spots = { 101:'Ferrari'
                 ,102:'Bugatti'
                 ,103:'Porsche'
                 ,104:'Mclaren'
                }

print(parking_spots.values())
print({parking_spots.values(): parking_spots.keys()})
switch = {parking_spots.values(): parking_spots.keys()}
print(switch)
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)
sDict = {x.upper(): x*3 for x in'coding'}
print (sDict)
nparray = np.arange(start=0, stop=6)
nparray
print(np.reshape(nparray, (2,3)))
print(np.arange(start=0, stop=11, step=2))

print(parking_spots.items())
print([(key[0], value[1]) for key, value in parking_spots.items()])
print([x for x in parking_spots.items()])
print([(x[0], x[1]) for x in parking_spots.items()])
print([x[0] for x in parking_spots.items()])
print(np.ones(shape=(3,2),dtype=int))
print(np.linspace(10, 40, 5,dtype=int))
print(np.empty(shape=(2,3)))

# chain a range and reshape
print(np.arange(start=1, stop=13).reshape((2,6)))

# Count the number of times the letter 's' appears in this string.
myquote = 'Slow is smooth, smooth is fast.'
print(myquote.count('s'), [myquote.index('s',1, 8), myquote[myquote.index('s',7,15):]])

# Country data
print(country_data.head(2))
print(country_data.iloc[2, :], country_data.iloc[2, :2])

# one column all rows, multiple columns w/slice (sequential), multiple columns with list of index column location is at (non-ordering available)
print(country_data.iloc[:, 0], '\n', country_data.iloc[:, 0:2], '\n', country_data.iloc[:, [0,3]])

# slice of rows
print(country_data.iloc[2:4 , :])

# Individual Rows or columns
print(country_data.iloc[[0,5], [0,2]])

print(country_data.iloc[:6, :3])

country_data.iloc[1:4, 0:3]

country_data.loc['JPN', 'country']
country_data.loc['JPN', :]

print([x for x in range(5)])


counter = 0
# make sure after running to reset counter variable if desired to see ouptut again
while counter < 4:
    print(counter)
    counter += 1

for i in ['hey', 'yo']:
    print(i)
    
# Use np.zeros to create a NumPy array filled with integers.
print(np.zeros(shape=4, dtype=int))


dimensions = ('x', 'y', 'z')

# Tuple unpacking : notice types 
dim1, dim2, dim3 = dimensions
print([type(dim1), dim1, type(dim2), dim2, type(dim3), dim3])
(dim4, dim5, dim6) = dimensions
print([type(dim4), dim4, type(dim5), dim5, type(dim6), dim6])

#Select two last items
car_list = ['ferrari','porsche','bugatti', 'pagani']
print(car_list[-2:])

# np full (2,4)
print(np.full(shape=(2,4), fill_value=7, dtype=int))

# np ones
print(np.ones(shape=(3,2), dtype=float))

#np arange
print(np.arange(start=1, stop=11))

print(np.arange(start=0, stop=11, dtype=int, step=2))

#np linspace
print(np.linspace(start=10, stop=40, num=4, dtype=int))

x = -3

if x > 0:
    print('greater than zero')
elif x == 0:
    print('equal to zero')
else:
    print('less than zero')
    
    
#Use a method to remove the period at the end of this string.
myquote = 'Slow is smooth, smooth is fast.'
myquote.strip('.')
myquote

# np linspace (0-100 in 4 increments (first output is 0))
print(np.linspace(start=0, stop=100, num=5, dtype=int))
hey = np.linspace(start=0, stop=100, num=5, dtype=int)
print(type(hey), hey, len(hey))


newdict = {x: x**3 for x in range(10) if x**3 %4 == 0}
# 0 and 1 skipped, 2**3 = 8, 8%4 == 0 (no remainder) {0:0, 2:8, 4:64, 6:216,  8:512}
print(newdict)
print(1**3)
print(2**3)
print(8%4)
print(8%2)
print(64%4)
print(36*6, 216%4)

npary = np.arange(start=0, stop=6, dtype=int)
print(npary)
print(np.reshape(npary, newshape=(2,3)))

print(np.arange(start=1, stop=11, dtype=int).reshape((2,5)))

print(country_data.head(10))

# Run code in a block not individually!
g = sns.scatterplot(data=country_data.loc['USA':'CAN', :], x='country', y='gdp', hue='continent')
g.set_xticklabels(labels=country_data.loc['USA':'CAN', :].index, rotation=45)
plt.show()


g_2 = sns.barplot(x=["Asia", "Africa", "Antartica", "Europe"],y=[90, 30, 60, 10])
g_2.set_xticklabels(
    labels=["Asia", "Africa", "Antartica", "Europe"], rotation=30)
# Show the plot
plt.show()






