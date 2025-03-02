#%%
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir("C:\\Users\\Sean\\Desktop\\Python\\ISLP_labs")

#import data into python
college = pd.read_csv('College.csv')
college
# %%
college3 = college.rename({"Unnamed: 0": 'College'},
                          axis=1)
college3

#%%
college3.describe()

# Select specific columns
columns_to_plot = ['Top10perc', 'Apps', 'Enroll']
selected_columns = college3[columns_to_plot]

# Produce scatterplot matrix
pd.plotting.scatter_matrix(selected_columns)
#%%
college3.boxplot("Outstate", "Private")

#%%
#create new qualitative variable 'Elite'
#binning Top10perc var into 2groups
college3["Elite"] = pd.cut(college3["Top10perc"],
                           [0, 50, 100],
                           labels=["No", "Yes"])
elite_counts = college3["Elite"].value_counts()
college3.boxplot('Outstate', "Elite")
#%%
# %%
#create histograms for all columns in DF
college3.hist(figsize=(10,10))
plt.tight_layout()
plt.show()