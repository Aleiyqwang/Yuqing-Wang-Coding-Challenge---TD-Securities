import pandas as pd
import matplotlib.pyplot as plt


# 1.	Read the csv file containing time series data and load it into a pandas dataframe
fx = pd.read_excel('Coding Challenge Data.xlsx', index_col="DATE")


# 2.a)	Calculate the daily percentage change for each currency pair.
fx_pct = fx.pct_change()
fx_pct = fx_pct.fillna(0)
print("daily percentage change for each currency pair \n", fx_pct.head())

# 2.b)	Calculate the moving average of the daily percentage change for a specified window size (for example, 5 days)
n = 5
fx_moving = fx_pct.rolling(n).mean()
print("moving average of the daily percentage change \n", fx_moving.head(10))


# 3.	Using a loop, iterate through the list of currency pairs and calculate the average
# daily percentage change for each pair over the entire dataset. Store the results in a dictionary.
fx_dict = {}
len_row, len_col = fx.shape
for i in range(len_col):
    for j in range(len_row-1):
        pct_change = (fx.iloc[j+1, i] - fx.iloc[j, i])/fx.iloc[j, i] * 100
        fx_dict[fx.columns[i]] = fx_dict.get(fx.columns[i], 0) + pct_change
    fx_dict[fx.columns[i]] = fx_dict[fx.columns[i]]/(len_row - 1)
print("percentage change for each pair over the entire dataset: \n", pd.DataFrame(fx_dict, index=["avg_change"]))


# 4.	Identify the currency pair with the highest average daily percentage change based on the calculated results.
highest = max(fx_dict, key=fx_dict.get)
print("The currency pair with the highest average daily percentage change is: ", highest)


# 5.	Plot the time series data for the currency pair identified in step 4.
ser = pd.Series(fx[highest], index=fx.index)
ser.plot()
plt.show()


# 6.	Bonus Question
cor = fx_pct.corr()  # correlation matrix
print("correlation matrix, USD/CAD has the highest correlation with AUD/USD \n", cor)

print("summary table of useful statistics \n", fx.describe())

bar = fx.head().plot.bar()
bar.set_yscale('log')
plt.show()
