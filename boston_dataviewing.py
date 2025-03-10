#%%
import pandas as pd
import os
import matplotlib.pyplot as plt

#set working directory
os.chdir("C:\\Users\\Sean\\Desktop\\Python\\ISLP_labs")

# %%
#load dataframe using absolute path of file location
#note difference between set directory and file location
boston = pd.read_csv("C:\\Users\\Sean\\Desktop\\Python\\ISLP_labs\\CSV_files\\Boston.csv")

print(boston.head())
#%%
#find number of observations in dataset
len(boston)
#506 observations

#find number of variables in the dataset
#.columns is a preloaded trait for dataframes in pandas
len(boston.columns)
#14 variables

#%%
#load some small plots for viewing
#NOX PP 10 Million and Crime Rates
plt.scatter(boston['nox'], boston['crim'])
plt.xlabel("NO2 Parts Per 10 Million")
plt.ylabel("Crime Rate per Capita by Town")
plt.show()

# %%
#Median home owner value and Crime Rates
plt.scatter(boston['medv'], boston['crim'])
plt.xlabel("Median Value of owner occupeied homes in $1000s")
plt.ylabel("Crime Rate per Capita by Town")
plt.show()

#%%
#find basic summary statistics of predictors 
boston.describe()
print(boston.describe())
'''
Some suburbs of Boston have relatively high rates of crime --> max = 88.97
Others are essentially non-existent --> min = 0.006320
Highest NOX value in Boston is 0.871000
Lowest NOX value is 0.385000
'''
#%%
#checking for number of observations marked located along Charles river
print(boston['chas'].value_counts())
#35 observations on river , 471 observations away from river

# %%
#find median value for pupil-teacher ratio
print(boston['ptratio'].describe())
#median value is 50% value in describe function --> 19.050000

#%%
#identify index (observation number) that has highest medv value
print(boston['medv'].idxmax())
max_medv = boston['medv'].idxmax()
#pull out values of all variables for observation with HIGHEST medv value
print(boston.loc[max_medv])

#identify index (observation number) that has lowest medv value
print(boston['medv'].idxmin())
min_medv = boston['medv'].idxmin()
#pull out values of all variables for observation with LOWEST medv value
print(boston.loc[min_medv])

#%%
#find the number of suburbs with avg rooms > 7
avg7 = sum( i > 7 for i in boston['rm'])
print(avg7)

#find number of suburbs with avg rooms > 8
avg8 = sum(i > 8 for i in boston['rm'])
print(avg8)
