##################################################
# LINEPLOT
#
# You'll learn:
# 
# - How to make line charts with the seaborn
#   lineplot() function
#
# - How to make a line chart with multiple lines
#
#
# © Copyright Sharp Sight, Inc.
# sharpsightlabs.com
# All rights reserved
#
##################################################


#----------------
# IMPORT PACKAGES
#----------------
import seaborn as sns
import pandas as pd



#---------------
# SET FORMATTING
#---------------
sns.set()



#----------------
# IMPORT DATASETS
#----------------
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank= pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')
stocks = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/stocks.csv')



# INSPECT
stocks.head()
stocks.shape[0]
print(stocks[stocks['stock'] == 'aapl'].shape[0])


#=======================================
# CONVERT 'date' FROM STRING TO DATETIME
#=======================================

stocks.date = pd.to_datetime(stocks.date)



#============
# SUBSET DATA
#============

#aapl_stock = stocks[stocks.stock == 'aapl']
aapl_stock = stocks.query("stock == 'aapl'")
aapl_stock.shape[0]

#--------
# INSPECT
#--------
aapl_stock.head()
print(aapl_stock.columns)
print(aapl_stock.date)



# CHECK UNIQUE VALUES
aapl_stock.stock.unique()
print(aapl_stock.index)
aapl_year_index = aapl_stock.set_index('date')
print(aapl_year_index.head(2))
print(aapl_year_index.sort_index())
appl_2005_2010 = aapl_year_index.sort_index().loc['2005-01-01':'2009-12-31', :]
print(appl_2005_2010.shape[0]) 
print(appl_2005_2010.tail(3))
#================
# PLOT LINE CHART
#================

sns.lineplot(data = aapl_stock
             ,x = 'date'
             ,y = 'close'
             )

#Subsetted years and passing index to x-axis
sns.lineplot(data=appl_2005_2010
             , x=appl_2005_2010.index
             , y='close'
             , hue='stock')


#==================
# CHANGE LINE COLOR
#==================

sns.lineplot(data = aapl_stock
             ,x = 'date'
             ,y = 'close'
             ,color = 'red'
             )



#===========================
# PLOT MULTI-LINE LINE CHART
#===========================

sns.lineplot(data = stocks
             ,x = 'date'
             ,y = 'close'
             ,hue = 'stock'
             )




# END