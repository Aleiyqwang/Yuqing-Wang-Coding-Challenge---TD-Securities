# read the data of Coding Challenge Data.xlsx
import pandas as pd
import numpy as np


# 1.	Read the csv file containing time series data and load it into a pandas dataframe
fx = pd.read_excel('Coding Challenge Data.xlsx', index_col="DATE")
#print(fx.head(10))

#print(fx.head())

# 2.a)	Calculate the daily percentage change for each currency pair. 
fx_pct = fx.pct_change()
fx_pct = fx_pct.fillna(0)
#print(fx_pct.head())

# 2.b)	Calculate the moving average of the daily percentage change for a specified window size (for example, 5 days)
n = 5
fx_moving = fx_pct.rolling(n).mean()
#print(fx_moving.head(10))

# 3.	Using a loop, iterate through the list of currency pairs and calculate the average 
# daily percentage change for each pair over the entire dataset. Store the results in a dictionary.

fx_dict = {}
len_row, len_col = fx.shape
for i in range(len_col):
    for j in range(len_row-1):
        pct_change = (fx.iloc[j+1, i] - fx.iloc[j, i])/fx.iloc[j, i] * 100
        fx_dict[fx.columns[i]] = fx_dict.get(fx.columns[i], 0) + pct_change
    fx_dict[fx.columns[i]] = fx_dict[fx.columns[i]]/(len_row - 1)
#print(pd.DataFrame(fx_dict, index=["avg_change"]))

# 4.	Identify the currency pair with the highest average daily percentage change based on the calculated results.
highest = max(fx_dict, key=fx_dict.get)
print("The currency pair with the highest average daily percentage change is: ", highest)

# 5.	Plot the time series data for the currency pair identified in step 4.

pd.Series(fx[highest], index = fx.index)