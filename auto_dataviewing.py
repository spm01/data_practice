#%%
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:\\Users\\Sean\\Desktop\\Python\\ISLP_labs")
# %%
#reading in data and dropping na values
auto = pd.read_csv("Auto.csv")
print(auto)
#replace ? with NaN
auto.replace('?', np.nan,inplace=True)
auto = auto.dropna()

#%%
#checking data types
print(auto.dtypes)
#horsepower is being viewed as object instead of int/float
auto['horsepower'] = pd.to_numeric(auto['horsepower'], errors='coerce')
#check if horsepower is now int/float
print(auto.dtypes)
#%%
#finding max and min values of each variable
auto.columns
print(auto.max())
print(auto.min())

# %%
#finding specific summary stats of each variable: mean and std
print(auto.describe().loc[['mean','std']])

# %%
#dropping 10-85 observations
#observe summary stat changes
auto_drop = auto.drop(auto.index[10:86])
print(auto.describe().loc[['mean','std','min','max']])
print(auto_drop.describe().loc[['mean','std','min','max']])
# %%
plt.scatter(auto['horsepower'],auto['mpg'])
plt.xlabel("Horsepower")
plt.ylabel("Miles per Gallon")
#set x-ticks based on range of horsepower
max_hp = int(auto['horsepower'].max()) 
plt.xticks(range(0, max_hp+10,25))
plt.yticks(range(0,50,5))
plt.show()

#%%
plt.scatter(auto['cylinders'],auto['mpg'])
plt.xlabel("Cylinders")
plt.ylabel("Miles per Gallon")
#set x-ticks based on range of cylinders
max_cyl = int(auto['cylinders'].max())
plt.xticks(range(0, max_cyl+3,2))
plt.yticks(range(0,50, 5))
plt.show()

# %%
plt.scatter(auto['weight'],auto['mpg'])
plt.xlabel("Weight")
plt.ylabel("Miles per Gallon")
max_weight = int(auto["weight"].max())
plt.xticks(range(1500, max_weight+500, 500))
plt.yticks(range(0,50,5))
plt.show()
