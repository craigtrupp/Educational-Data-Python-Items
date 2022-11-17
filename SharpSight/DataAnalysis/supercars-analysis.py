#######################################################
# DATA EXPLORATION AND ANALYSIS 
#  with Pandas, Seaborn, and Python
#
# Here, we will be implementing the strategy:
#  Overview first, zoom and filter, details on demand
#
# Steps:
# - You should have questions to start off with
# - Inspect your data
# - Asking questions of your data
# - Overview first, zoom and filter, details on demand
#
#
# sharpsightlabs.com
# © Copyright Sharp Sight
# All rights reserved
#
#######################################################


#----------------
# IMPORT PACKAGES
#----------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# set plot formatting
plt.style.use('fivethirtyeight')
sns.set(rc = {'figure.figsize':(12,8)})

#------------
# IMPORT DATA
#------------
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')


#========================================
# EXAMINE DATA
# - get a little more clarity about the
#   exact contents of the data
# - This will help tell you what you can
#   and can't answer with this dataset
#========================================

#---------------------------------------------
# PRINT OUT THE FIRST FEW RECORDS
# - look at variables
# - Visually inspect values
#   (missing, etc.)
# - check that values match your expectations
#   based on knowledge of the data
#---------------------------------------------

supercars.head()


#-------------------------------------
# EXAMINE THE "STRUCTURE" OF THE DATA
#-------------------------------------

supercars.columns
# Index(['model', 'make', 'year', 'decade', 'horsepower', 'torque',
#        'seconds_0_60', 'engine_size', 'top_speed', 'weight'],
#       dtype='object')


supercars.shape
# (1578, 10)


supercars.dtypes
# model            object
# make             object
# year              int64
# decade           object
# horsepower        int64
# torque          float64
# seconds_0_60    float64
# engine_size     float64
# top_speed       float64
# weight          float64
# dtype: object



#------------------------------
# Inspect categorical variables
#------------------------------

# GET UNIQUE VALUES for a few sample columns above listed in the dtypes output showing the columns data type
supercars.decade.unique()
supercars.make.unique()


# GET FREQUENCY COUNTS
(supercars
  .decade
  .value_counts()
)

# GET FREQUENCY COUNTS
(supercars
  .year
  .value_counts()
)

(supercars
  .make
  .value_counts()
)


# SORT (Year down)
supercars = (supercars
             .sort_values('year', ascending = False)
             .reset_index(drop = True) # drop old index column that's add by default to a new column with method
             )

print(supercars[['year']].value_counts())

#====================================================================
# PRELIMINARY: ASK QUESTIONS 
#
# When you approach a dataset, you should already have things in mind.
# Its very rare to approach a dataset with no questions.
# 
#
# Frequently, there are a few variables that you'll be interested in.
#  - i.e., key metrics
#  - Initial data inspection will help you understand which variables
#    to focus on
#
#
#--------------
# QUESTION LIST 
#--------------
# - What is the relationship between horsepower and speed?
# - How is car speed distributed?  
# - What is a "really really fast car?"
# - What is the relationship between horsepower and 0-60 time?
# - How has car speed changed over time?
# - Who is making the fastest cars today?
#   
#
#--------------------
# IMPORTANT VARIABLES
#--------------------
# - top_speed
# - seconds_0_60
# - year (for possible trending)
# - decade (for possible trending)
# - make
# - model
#
#===============================================================




#=============================================================
# VISUAL DATA INSPECTION & ANALYSIS
#----------------------------------
# 
# Typically, well start with "overview" charts: 
# - look at single variables first
# - Bar charts for categorical vars
# - Histograms for numerical vars
# 
#
# At every step, we're looking for anything unusual.
# When we find something, we'll have a new question.
# - a new place to "dive in"
#
#
# You won't always find new or interesting things, 
# and that's OK.  At least 80% of your work will probably be
# "same old stuff" but you'll report on it anyway.
#
# As we begin to examine our data and find "interesting things"
# we will "zoom & filter" to dig in.
# 
# If we choose, we'll get details as well.
#
#---------------------------------------------------------------




#==============================================
# OVERVIEW FIRST
#
# You should know which variables you want to 
# focus on after initial inspection
# and question generation
# 
# What are we looking for?
# - trends (up, down)
# - spikes
# - "big changes"
# - outliers
# - "unusual" features
#
# ...These will all help us answer questions
#    and refine our questions
#==============================================

#------------------------------------------------------------------
# BASIC HISTOGRAMS (single variables)
# - we use histograms to look at distribution of numeric variables
#------------------------------------------------------------------


#------------------------------------
# CAR SPEED
# - Q: How is car speed distributed
#------------------------------------

sns.histplot(data = supercars, x = 'top_speed')

# NOTE: Spike in top speed around 155
#    Q: what is this?


#------------
# Horsepower
#------------
sns.histplot(data = supercars, x = 'horsepower')


#------------
# Torque
#------------
sns.histplot(data = supercars, x = 'torque')


## Torque and Horsepower each skew a bit right (tail off to right with a few outliers) but more normal than top_speed spike


#--------------------------------------------------------------
# HP per tonne
# - note, we're using Pandas .assign() to create a new variable
#   and we're using the output directly inside sns.histplot()
#    in order to plot it
#--------------------------------------------------------------

sns.histplot(
    data = (supercars
             .assign(hp_per_ton = supercars.horsepower / supercars.weight)
            )
    ,x = 'hp_per_ton'
    )


#---------------------------------------
# YEAR
# - note: the years are in proper order
#---------------------------------------

sns.countplot(data = supercars
              ,x = 'year'
              ,color = 'red'
              )
plt.xticks(rotation = 90, size = 12)

## Counting categorical data ( a value_counts call would show the numeric table representation)
# =============================================================================
# print(supercars[['year']].value_counts())
# year
# 2012    97
# 2013    94
# 2006    70
# 2009    64
# 
# =============================================================================


## Bivariate Analysis
#===============================
# SCATTER (2 numeric variables)
#===============================

#-------------------------------------------------------------
# HORSEPOWER vs SPEED 
# - Q: What is the relationship between horsepower and speed?
#-------------------------------------------------------------

sns.scatterplot(data = supercars
                ,x = 'horsepower'
                ,y = 'top_speed'
                )

# NOTE: "stripe" around 150 again
# Q: Did that spike appear at a specific time? Decade?


#---------------------
# HORSEPOWER vs TORQUE
#---------------------

sns.scatterplot(data = supercars
                ,x = 'horsepower'
                ,y = 'torque'
                )



#==============================================================
# ZOOMING AND FILTERING
# - Use query()
# - Use categorical variables to "cut" or "break out" our data
#==============================================================


#------------------------------------------------
# "CUT" BY CATEGORICAL
# - Q: How has car speed changed over time
# - Q: When did that "spike" appear in the data
# - facet with categorical variables
# - here, we're moving into multivariate
#   views
#------------------------------------------------

(sns.FacetGrid(data = supercars, col = 'decade', col_wrap = 4)
    .map(sns.histplot, 'top_speed')
)



#---------------------------------------
# QUERY: 1990s to 2000s only
# - Here, we're using query() to
#   zoom in on the unusual feature
#   at top_speed about equal to 150
#---------------------------------------

sns.histplot(
    data = (supercars
             .query('decade == "2000s" | decade == "1990s"') # or operator to get supercars for either year
            )
    ,x = 'top_speed'
    )
print(len(supercars.query('decade == "2000s" | decade == "1990s"')))

#---------------------------------
# "ZOOM" in on interesting feature
#  - filter data:
#  - speed between 149 and 159
#---------------------------------

(supercars
    .query('decade == "2000s" | decade == "1990s"')
    .query('top_speed > 149 & top_speed < 159')
)

## chain query methods for multiple filtered dataframes 
## This is zooming in on the spike revealed in the histogram of a peak of about 155-160 
## Isolated decade in a FacetGrid Hist type distribution to reveal the decaded with the highest count for our second query targe (top_speed)


sns.histplot(
    data = (supercars
             .query('decade == "2000s" | decade == "1990s"')
             .query('top_speed > 149 & top_speed < 159')
            )
    ,x = 'top_speed'
    )


# Here, we've found something
# - big spike at 155
# - now, RESEARCH
# - talk to Subject Matter Experts (SMEs),
#   partners, and do some searching



#-------------------------------
# TABLE OF CAR COMPANIES WITH 
#  CARS AT MAX SPEED = 155
#-------------------------------

(supercars
    .query('decade == "2000s" | decade == "1990s"')
    .query('top_speed == 155')
    .filter(['make'])
    .value_counts()
)



#==============================
# TOP CAR MAKERS OF FAST CARS
# - Q: Who makes fast cars?
#==============================

#--------------
# CREATE TABLE
#--------------

(supercars 
    .filter(['make','top_speed'])
    .groupby(['make'])
    .agg({'top_speed':'max'})
    .sort_values('top_speed', ascending = False)
)

# =============================================================================
#             top_speed
# make                 
# Koenigsegg      273.0
# SSC             273.0
# Hennessey       260.0
# Bugatti         258.0

# [99 rows x 1 columns]
# =============================================================================

print(supercars['make'].nunique()) # 99

#------------------------
# PLOT DATA WITH GGPLOT2
#------------------------


bar_data = (supercars 
    .filter(['make','top_speed'])
    .groupby(['make'])
    .agg('max') # not necessary to pass dict with non filtered group by column (top_speed) - done above to add context or for quick reference
    .sort_values('top_speed', ascending = False)
    .iloc[0:10] ## Grabbing top ten from output above for top speed by make
    .reset_index()
)

sns.barplot(data = bar_data
            ,y = 'make'
            ,x = 'top_speed'
            ,color = 'darkred'
            )


# REDO, USING PANDAS + SEABORN COMBINED
sns.barplot(data = (supercars 
                    .filter(['make','top_speed'])
                    .groupby(['make'])
                    .agg('max')
                    .sort_values('top_speed', ascending = False)
                    .iloc[0:10]
                    .reset_index()
                    )           
            ,y = 'make'
            ,x = 'top_speed'
            ,color = 'darkred'
            )

## Alternative way to avoid memory/new dataframe creation (bar_data) with passing the ouptut to data parameter above

#===============================
# Q: What are the fastest cars?
# Bar Chart
#  top 10 fastest cars
#===============================

#------------
# MAKE TABLE
#------------
(supercars
    .filter(['model','top_speed'])
    .sort_values('top_speed', ascending = False)
    .iloc[0:10]
)


#                                         model  top_speed
# 2                        SSC Ultimate Aero TT      273.0
# 3                   Koenigsegg Agera R 5.0 V8      273.0
# 5                      Koenigsegg Agera 5L V8      261.0
# 6                          Hennessey Venom GT      260.0
# 0    Bugatti Veyron 8.0 litre W16 Super Sport      258.0
# 4                            Porsche 9FF GT9R      256.0
# 10                            Porsche 9FF GT9      255.0
# 1     Bugatti Veyron 16.4 Grand Sport Vitesse      255.0
# 8   Koenigsegg CCX R Special Edition 4.8 V8 S      254.0
# 9                Bugatti Veyron 8.0 litre W16      252.0


#------------------------
# PLOT DATA WITH SEABORN
#------------------------

sns.barplot(data = (supercars
                    .filter(['model','top_speed'])
                    .sort_values('top_speed', ascending = False)
                    .iloc[0:10]
                    )
            ,y = 'model'
            ,x = 'top_speed'
            ,color = 'darkred'
            )



#===========================================
# EVOLUTION OF CAR SPEED OVER TIME
# (as seen by fastest car every year)
# - Q: How has car speed changed over time
#===========================================

#-------
# TABLE
#-------

(supercars 
  .filter(['year','top_speed'])
  .groupby(['year'])
  .agg('max')
)

# =============================================================================
#       top_speed
# year           
# 1939      125.0
# 1947      124.0
# 1948      125.0
# 1949      102.0
# =============================================================================


#------------------------
# PLOT DATA WITH GGPLOT2
#------------------------

sns.scatterplot(data = (supercars 
                        .filter(['year','top_speed'])
                        .groupby(['year'])
                        .agg('max')
                        )
                ,x = 'year'
                ,y = 'top_speed'
                )


#-----------------
# ADD SMOOTHE LINE
#-----------------
sns.regplot(data = (supercars 
                        .filter(['year','top_speed'])
                        .groupby(['year'])
                        .agg('max')
                        .reset_index()
                        )
            ,x = 'year'
            ,y = 'top_speed'
            ,lowess = True
            ,line_kws = {'color':'red'}
            )



#========================================
# 0-to-60 by Horsepower
# - Q: What is the relationship between 
#      0-60 and engine power?
#========================================

sns.scatterplot(data = supercars
                ,x = 'horsepower'
                ,y = 'seconds_0_60'
                )


# NOTE: The data are slightly overplotted ... 
#       we will alpha to mitigate this

sns.scatterplot(data = supercars
                ,x = 'horsepower'
                ,y = 'seconds_0_60'
                ,alpha = .5
                )


# ADD SMOOTH LINE
sns.regplot(data = supercars
                ,x = 'horsepower'
                ,y = 'seconds_0_60'
                ,lowess = True
                ,scatter_kws = {'alpha':.5}
                ,line_kws = {'color':'red'}
                )


  
#========================================================
# RECAP:
# - Ask questions
# - Know your data
# - Refine your questions
# - "Overview first, zoom and filter, details on demand"
#========================================================