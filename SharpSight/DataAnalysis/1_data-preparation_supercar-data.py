##############################################
# DATA PREPARATION WITH THE TIDYVERSE
#
# How to ...
#   - collect raw datasets
#   - clean them up 
#   - join them together
#   - inspect for accuracy
#
#
# sharpsightlabs.com
# © Copyright Sharp Sight, Inc.
# All rights reserved
#
##############################################



#================
# LOAD LIBRARIES
#================
import pandas as pd



#=================
# IMPORT datasets 
#=================

car_torque = pd.read_csv("https://www.sharpsightlabs.com/datasets/car_data/car_torque.txt")
car_0_60_times = pd.read_csv("https://www.sharpsightlabs.com/datasets/car_data/car_0-60-times.txt")
car_horsepower = pd.read_csv("https://www.sharpsightlabs.com/datasets/car_data/car_horsepower.txt")
car_top_speed = pd.read_csv("https://www.sharpsightlabs.com/datasets/car_data/car_top-speed.txt")
car_power_to_weight = pd.read_csv("https://www.sharpsightlabs.com/datasets/car_data/car_power-to-weight.txt")
car_engine_size = pd.read_csv("https://www.sharpsightlabs.com/datasets/car_data/car_engine-size.txt", sep = ";")



#==============
# INSPECT DATA
#==============

# INSPECT WITH head()
car_torque.head()
car_0_60_times.head()
car_engine_size.head()
car_horsepower.head()
car_top_speed.head()
car_power_to_weight.head()


# INSPECT WITH describe()
car_torque.describe()
car_0_60_times.describe()
car_engine_size.describe()
car_horsepower.describe()
car_top_speed.describe()
car_power_to_weight.describe()



#=====================================================================
# LOOK FOR DUPLICATE RECORDS 
# - duplicate records are problematic when
#   we perform joins
# - if we have duplicate records in the 'raw' data
#   we will have dupes in the final data
# - you always want to look for dupes before you
#   join your datasets
# 
# Details: 
# - we're using groupby() to aggregate by the car name (car_full_nm)
# - agg() counts the total records, by car name
# - query() is looking for rows with duplicates
#=====================================================================


#-----------------------------------------
# TEST
# - we'll use part of our dupe-check code
#   but only to look at the structure
# - the output shows each car 
#   and the number of records for each car
#-----------------------------------------
print(car_torque.columns.tolist(), car_torque.dtypes)

car_torque_test = car_torque.assign(count=1)
print(car_torque_test['car_full_nm'].value_counts(ascending=False))
print(car_torque_test.groupby('car_full_nm').agg('sum'))

# This is ony to evaluate, not updated the car_torque dataframe. Prototype to 
(car_torque
 .assign(count = 1)
 .groupby('car_full_nm')
 .agg({'count':'sum'})
 .sort_values('count', ascending=False)
)


# Code Detail
# =============================================================================
# Assign a new column named count with a value of 1 to each row
# Groupby car full name to see if car exists more than one in dataframe
# perform aggregate function 'sum' on created count column for each groupby dataframe to see if multiple car_names can be found
# Sort values by the aggregated sum on the created column to see which cars may have the most counts
# =============================================================================



#-----------
# FIND DUPES
#-----------

car_horsepower.assign(count = 1).groupby('car_full_nm').agg({'count':'sum'}).query('count != 1')
car_torque.assign(count = 1).groupby('car_full_nm').agg({'count':'sum'}).query('count != 1')
car_0_60_times.assign(count = 1).groupby('car_full_nm').agg({'count':'sum'}).query('count != 1')
car_engine_size.assign(count = 1).groupby('car_full_nm').agg({'count':'sum'}).query('count != 1')
car_top_speed.assign(count = 1).groupby('car_full_nm').agg({'count':'sum'}).query('count != 1')
car_power_to_weight.assign(count = 1).groupby('car_full_nm').agg({'count':'sum'}).query('count != 1')

# Code Detail
# =============================================================================
# Similar to above car torque were are assigning a new column to each row prior to groupby by the name and performing aggregate sum for 
# that grouped by counts (which was set to 1 for each row). Then the .query is chained to looked at the created count column to find rows
# in the groupby dataframe that have multiple records or != 1
# =============================================================================




# NOTE: duplicate records!
# several datasets have duplicate rows for the following cars (car_full_nm)

# Chevrolet Chevy II Nova SS 283 V8 Turbo Fire - [1964]     2
#           Koenigsegg CCX 4.7 V8 Supercharged - [2006]     2
#                   Pontiac Bonneville 6.4L V8 - [1960]     2



#----------------------------------------
# EXAMINE DUPES
# - here, we're actually looking at the
#   duplicate rows
# - to do this, we're using query()
#   to retrieve the rows in question
#----------------------------------------

## Car_full_nms look to have more than 1 count from the groupby dataframe from various cars ones above

car_top_speed.query('car_full_nm == "Chevrolet Chevy II Nova SS 283 V8 Turbo Fire - [1964]"') # Note different top speed 
car_top_speed.query('car_full_nm == "Koenigsegg CCX 4.7 V8 Supercharged - [2006]"') # Looks like dupe
car_top_speed.query('car_full_nm == "Pontiac Bonneville 6.4L V8 - [1960]"') # Looks like dupe



# NOTES:
# - The Chevy has 2 dissimilar records, which is unusual.  For simplicity, we will just choose 1
# - The Koenigsegg has 2 identical records
# - The Pontiac has 2 identical records



#==============================================
# DEDUPE DATA 
# - here, we're actually removing the rows
#   using drop_duplicates()
# - note: this is the quick-and-dirty
#   way of removing dupes
# - we could also do this manually to 
#   have more control over exactly which of the
#   duplicates get removed
#==============================================

# Any car name with more than one record is deleted with the first fournd car name kept and all other rows deleted (subset is the column to look for dupes)
# Reassigning used variable names to dropped duplicates dataframes for any multiple car_full_nm in any dataset

car_0_60_times  = car_0_60_times.drop_duplicates(subset = 'car_full_nm', keep = 'first')
car_engine_size = car_engine_size.drop_duplicates(subset = 'car_full_nm', keep = 'first')
car_horsepower  = car_horsepower.drop_duplicates(subset = 'car_full_nm', keep = 'first')
car_top_speed   = car_top_speed.drop_duplicates(subset = 'car_full_nm', keep = 'first')
car_torque      = car_torque.drop_duplicates(subset = 'car_full_nm', keep = 'first')
car_power_to_weight = car_power_to_weight.drop_duplicates(subset = 'car_full_nm', keep = 'first')



#================================
# RE-INSPECT DUPES
# -are the dupes removed? (Yes.)
#================================

car_top_speed.query('car_full_nm == "Chevrolet Chevy II Nova SS 283 V8 Turbo Fire - [1964]"')
car_top_speed.query('car_full_nm == "Koenigsegg CCX 4.7 V8 Supercharged - [2006]"')
car_top_speed.query('car_full_nm == "Pontiac Bonneville 6.4L V8 - [1960]"')



len(car_horsepower)      # 1578  * This is the longest, and the most 'important'
                         #         so we'll use it as the 'base' table
                         #         as we start to join the datasets all together
len(car_torque)          # 1577
len(car_0_60_times)      # 398
len(car_engine_size)     # 1576
len(car_top_speed)       # 1570
len(car_power_to_weight) # 1587



#=================================================
# JOIN DATA 
# - df.car_specs is sort of a master dataset
# - the first join joins two of the datasets
# - each additional dataset appends new variables
#   from the newly joined data
#=================================================


#---------------------------------------------------------------------------------
# JOIN
# - we're joining the data frames together, 2 at a time
# - note that car_horsepower is the first dataset in the first merge()
#   ... this is because we just identified it as the longest/most-important table
#       which we can use as the foundation of our new master-dataset
#---------------------------------------------------------------------------------
print(car_horsepower.columns, car_torque.columns)
print(car_horsepower.merge(car_torque, on='car_full_nm', how='left')) # all from largest dataframe (car_horsepower) with extra columns from torque 
print(car_horsepower.merge(car_torque, on='car_full_nm', how='left').columns.tolist())

# =============================================================================
# Series of merge/db joins below are to use the base dataframe with most rows (horsepower)
# and merge/join with other dataframe to growing merged dataframe on like key index (car_full_nm)
# This is in effect widening our dataframe to include our dframe with most rows and a series of left joins to include all rows from our base table/df
# and their other columns
# =============================================================================

car_specs = car_horsepower.merge(car_torque, on = 'car_full_nm', how = 'left')  # count after join: 1578
car_specs = car_specs.merge(car_0_60_times, on = 'car_full_nm', how = 'left')   # count after join: 1578
car_specs = car_specs.merge(car_engine_size, on = 'car_full_nm', how = 'left')  # count after join: 1578
car_specs = car_specs.merge(car_top_speed, on = 'car_full_nm', how = 'left')    # count after join: 1578
car_specs = car_specs.merge(car_power_to_weight, on = 'car_full_nm', how = 'left') # count after join: 1578
print(len(car_specs), car_specs.columns)

## How many null columns values do we have now after our joins
print(car_specs.isna().sum()) ##

## We can see here that our tables with few rows after a left join resulted in many nulls for cars only in our left table and not in smaller right table/dframe
# =============================================================================
# car_full_nm                        0
# horsepower_bhp                     0
# rpm_horsepower_measure_point       0
# torque_lb_ft                       2
# rpm_torque_measure_point           2
# car_0_60_time_seconds           1181
# engine_size_cc                     5
# engine_size_ci                     5
# top_speed_mph                     10
# top_speed_kph                     10
# horsepower_per_ton_bhp             0
# dtype: int64
# =============================================================================
print(len(car_0_60_times))
print(len(car_horsepower) - len(car_0_60_times))

## Just an idea here what the likely result of the highest null count for this column in our agg dataset based on it's initial length
# =============================================================================
# 398
# 1180
# =============================================================================


#--------------------------
# RE-EXAMINE DUPES
# - they should be gone ...
#--------------------------

(car_specs
 .assign(count = 1)
 .groupby('car_full_nm')
 .agg('sum')
 .query('count != 1')
)


# Empty DataFrame
# Columns: [horsepower_bhp, rpm_horsepower_measure_point, torque_lb_ft, rpm_torque_measure_point, car_0_60_time_seconds, engine_size_cc, engine_size_ci, top_speed_mph, top_speed_kph, horsepower_per_ton_bhp, count]
# Index: []

## Fantastic! No similar multiple count found for our aggregated dataset that have had it's orignal dataframe dup rows removed based on multiple foun car_full_nm in our groupby examination chained methods

#----------------
# Re-inspect data
#----------------

car_specs.head()
car_specs.describe()
car_specs.describe(include='all')
car_specs.dtypes



# Observations: 1,578
# car_full_nm                      object
# horsepower_bhp                    int64
# rpm_horsepower_measure_point      int64
# torque_lb_ft                    float64
# rpm_torque_measure_point        float64
# car_0_60_time_seconds           float64
# engine_size_cc                  float64
# engine_size_ci                  float64
# top_speed_mph                   float64
# top_speed_kph                   float64
# horsepower_per_ton_bhp          float64
# dtype: object



#=================
# RENAME VARIABLES
#=================

car_specs.columns

car_specs = car_specs.rename(columns = {
        'horsepower_bhp':'horsepower'
        ,'torque_lb_ft':'torque'
        ,'car_0_60_time_seconds':'seconds_0_60'
        ,'engine_size_ci':'engine_size'
        ,'top_speed_mph':'top_speed'
        ,'car_weight_tons':'weight'
        })

car_specs.columns

# =============================================================================
# Index(['car_full_nm', 'horsepower', 'rpm_horsepower_measure_point', 'torque',
#        'rpm_torque_measure_point', 'seconds_0_60', 'engine_size_cc',
#        'engine_size', 'top_speed', 'top_speed_kph', 'horsepower_per_ton_bhp'],
#       dtype='object')
# =============================================================================




#===================
# ADD NEW VARIABLES
#===================

#-------------------------------
# NEW VAR: year
# - we will use str_sub() 
#   to strip the year out of the
#-------------------------------


# TEST
## Year value with the car_full_name (use str.slice) is at the end of the string - let's get the year value

## Let's see where the year value is (both below return same output)
car_specs.iloc[:5, :].loc[:, 'car_full_nm']
car_specs[:5]['car_full_nm']

# =============================================================================
# 0    Bugatti Veyron 8.0 litre W16 Super Sport - [2010]
# 1     Bugatti Veyron 16.4 Grand Sport Vitesse - [2012]
# 2                        SSC Ultimate Aero TT - [2008]
# 3                   Koenigsegg Agera R 5.0 V8 - [2012]
# 4                            Porsche 9FF GT9R - [2009]
# =============================================================================

car_specs.car_full_nm.str.slice(start = -5, stop = -1) # LOOKS GOOD!

# =============================================================================
# 0       2010
# 1       2012
# 2       2008
# =============================================================================


# CREATE VAR
car_specs = car_specs.assign(year = car_specs.car_full_nm.str.slice(start = -5, stop = -1) )


# INSPECT (look at new year column created above)
car_specs.head()
car_specs.year.dtype # dtype('O') strings


# EXAMINE LEVELS
car_specs.year.unique() # unique years found for the newly created column above



#----------------
# NEW VAR: decade
#----------------

# CREATE MAPING FUNCTION
def map_values(row, values_dict):
    return values_dict[row]

# DEFINE MAPPING DICTIONARY
decade_mapping = { '193': '1930s'
                  ,'194': '1940s'
                  ,'195': '1950s'
                  ,'196': '1960s'
                  ,'197': '1970s'
                  ,'198': '1980s'
                  ,'199': '1990s'
                  ,'200': '2000s'
                  ,'201': '2010s'
                  }


# CREATE DECADE VARIABLE
# .apply (similar to a map function) - we pass the function map_values to apply to each column or row (default)
# args = tuple of positional arguments to pass to func in addition*** to array/series (aka row) 

## One iteration (would take first row, slice the year column to a **decade holder value (first 3 values of respective 'year' column value for row))
## once sliced, the value is passed to the apply method which will provide the create slice value as the first argument (or row above in map_values function)
## lastly the apply method also takes the args tuple parameter to match the sliced value passsed to the method by default to the provided dictionary in the args function
car_specs = car_specs.assign(decade = car_specs.year.str.slice(0,3).apply(map_values, args = (decade_mapping,)))


# INSPECT decade
pd.set_option('display.max_rows', 70)
(car_specs
 .filter(['year','decade'])
 .drop_duplicates()
 .sort_values('year')
 .reset_index(drop = True)
)

## Subset to inspect dataframe to review if decade column assigning produced the mapping values based on the sliced string value of the created year column
# =============================================================================
#     year decade
# 0   1939  1930s
# 1   1947  1940s
# 2   1948  1940s
# 3   1949  1940s
# 4   1950  1950s
# 5   1951  1950s
# 6   1952  1950s
# 7   1953  1950s
# 8   1954  1950s
# 9   1955  1950s
# =============================================================================

#--------
# INSPECT
#--------

car_specs.head()


#-------------------------------
# NEW VAR: make 
#  (i.e., the "make" of the car; 
#  the "brand name" of the car) 
#-------------------------------

## Look for first empty space and strip everthhing else to get just the first part of the string as the car make from the car_full_nm
car_specs = car_specs.assign(make = car_specs.car_full_nm.str.replace(" .*$",""))



# CHECK UNIQUE VALUES
# - do these car makes look correct? (Yes)
# - anything unusual? (No)

pd.set_option('display.max_rows', 100)
(car_specs
 .filter(['make'])
 .drop_duplicates()
 .sort_values('make')
 .reset_index(drop = True)
)

## Makes
# =============================================================================
# 
#               make
# 0               AC
# 1              AMC
# 2       Alfa-Romeo
# 3           Alpine
# 4            Ariel
# 5           Ascari
# 6     Aston-Martin
# 7             Audi
# 8    Austin-Healey
# =============================================================================


#---------------
# NEW VAR: model 
#---------------

car_specs = car_specs.assign(model = car_specs.car_full_nm.str.replace("(^[^\s]+\s)(.*)(\s-\s.*$)","\\2"))



# CHECK UNIQUE VALUES
# - do these car makes look correct? (Yes)
# - anything unusual? (No)

pd.set_option('display.max_rows', 100)
(car_specs
 .filter(['model'])
 .drop_duplicates()
 .sort_values('model')
 .reset_index(drop = True)
)

# =============================================================================
#                                model
# 0     1 Series 123d 2d Coupe M-Sport
# 1     1 Series 135i 2d Coupe M-Sport
# 2                 1 Series M135i F20
# 3              100 2.2 Turbo Quattro
# 4                            100 BN1
# =============================================================================




#----------------
# NEW VAR: weight 
#----------------

car_specs = car_specs.assign(weight = car_specs.horsepower / car_specs.horsepower_per_ton_bhp) # assignment done by row
car_specs_two = car_specs[:1][['horsepower', 'horsepower_per_ton_bhp']]
print(car_specs_two)
# =============================================================================
#    horsepower  horsepower_per_ton_bhp
# 0        1184                   644.1
# =============================================================================
print(car_specs[:1][['horsepower', 'horsepower_per_ton_bhp', 'weight']])
# =============================================================================
#    horsepower  horsepower_per_ton_bhp    weight
# 0        1184                   644.1  1.838224
# =============================================================================

## Important Note (If wanting to apply function across a dataframe row, make sure to pass axis=1 to have access to the column names)
weight_manual = car_specs_two.apply(lambda x: x['horsepower']/x['horsepower_per_ton_bhp'], axis=1)
car_specs_two['weight_manual'] = car_specs_two.apply(lambda x: x['horsepower']/x['horsepower_per_ton_bhp'], axis=1)

print(car_specs_two)
# =============================================================================
#    horsepower  horsepower_per_ton_bhp  weight_manual
# 0        1184                   644.1       1.838224
# =============================================================================




#-------------------------
# NEW VAR: torque_per_ton 
#-------------------------

car_specs = car_specs.assign(torque_per_ton = car_specs.torque / car_specs.weight)



#=====================
# REORDER VARIABLES &
# DROP EXTRA VARIABLES
#=====================

car_specs = car_specs.filter(['make'
                              ,'model'
                              ,'year'
                              ,'decade'
                              ,'horsepower'
                              ,'torque'
                              ,'seconds_0_60'
                              ,'engine_size'
                              ,'top_speed'
                              ,'weight']
        )



#========================================
# INSPECT DATA
#  - quick checks to make sure that
#    the variables were created properly
#========================================

# head(df.car_specs)
car_specs.head()

## Validate New Weight or column assignments above
# =============================================================================
#          make                             model  ... top_speed    weight
# 0     Bugatti  Veyron 8.0 litre W16 Super Sport  ...     258.0  1.838224
# 1     Bugatti   Veyron 16.4 Grand Sport Vitesse  ...     255.0  1.990250
# 2         SSC                  Ultimate Aero TT  ...     273.0  1.250000
# 3  Koenigsegg                    Agera R 5.0 V8  ...     273.0  1.415082
# 4     Porsche                          9FF GT9R  ...     256.0  1.346154
# =============================================================================
car_specs.describe()
## Describe numeric values for box plot type values for each column
# =============================================================================
#         horsepower       torque  ...    top_speed       weight
# count  1578.000000  1576.000000  ...  1568.000000  1578.000000
# mean    304.655894   301.180838  ...   150.194515     1.476125
# std     163.010440   150.155085  ...    28.850534     0.422622
# min      34.000000    41.000000  ...    74.000000     0.450010
# 25%     191.250000   192.000000  ...   131.000000     1.230166
# 50%     275.000000   276.000000  ...   149.000000     1.445246
# 75%     389.750000   391.000000  ...   158.000000     1.690080
# max    1184.000000  1106.000000  ...   273.000000     6.360947
# =============================================================================

#------------------------------
# Frequency table (AGGREGATE) 
#  - decade                   
#------------------------------

# CHECK 'decade' variable
  
(car_specs
 .filter(['decade'])
 .assign(count = 1)
 .groupby('decade')
 .agg({'count': 'sum'})
)



# decade count
# 1930s     2
# 1940s     7
# 1950s    57
# 1960s   143
# 1970s   125
# 1980s   154
# 1990s   262
# 2000s   526
# 2010s   302


#------------------------------
# Frequency table (AGGREGATE) 
#  - make                     
#------------------------------

(car_specs
 .filter(['make'])
 .assign(count = 1)
 .groupby('make')
 .agg('sum')
 .sort_values('count', ascending = False)
)

## Snippet to groupby the make to see the total counts of different makes
# =============================================================================
#                 count
# make                 
# Ford              110
# Audi               98
# Porsche            95
# BMW                91
# Mercedes           90
# Ferrari            64
# Subaru             53
# =============================================================================




car_specs.head()




# EOF