# Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017 about the S&P 500 closing prices as well as some other financial indicators, including the “Long Term Interest Rate”, which is interest rate paid on 10-year U.S. government bonds.

# Write a program that computes the average closing price (the second column, labeled SP500) and the highest long-term interest rate. Both should be computed only for the period from June 2016 through May 2017. Save the results in the variables mean_SP and max_interest.


# 2 and 6 ([1, 5]) for SP500 and Long Interest Rate
# datetime would be handy! (Although can't import into runtime environment)
#from datetime import datetime as dt : import acting wonky (no surprise though)
sp_500_jn16_may17 = []
max_interest = 0
with open('SP500.txt', 'r') as f:
    #print(f.read())
    price_data = f.readlines()[1:] # can still readlines after reading file
    for row in price_data: # Loop Through Rows
        #print(row)
        columns_lst = row.split(',') # Set Default Col values for row
        date = columns_lst[0]
        date_lst = columns_lst[0].split('/')
        date_month, date_year = int(date_lst[0]), int(date_lst[-1])
        sp_500 = columns_lst[1]
        lintrs_rt = columns_lst[5]
        #print(date_lst, date_month, date_year)
        if (date_month >= 6 and date_year == 2016) or (date_month <= 5 and date_year == 2017):
            sp_500_jn16_may17.append(float(sp_500)) # need to transform to a float
            if float(lintrs_rt) > max_interest:
                max_interest = float(lintrs_rt)
        
                
mean_SP = sum(sp_500_jn16_may17) / len(sp_500_jn16_may17)
print(sp_500_jn16_may17)
print(mean_SP)
print(max_interest)