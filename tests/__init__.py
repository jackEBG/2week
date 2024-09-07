import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import zscore

def missing_values(df):
#total missing values
mis_val = df.isnull().sum()
miss_valPercent= 100 * df.isnull().sum / len(df)
#data type missing values
mis_val_dtype = df.dtypes
#make the table with the result
mis_valTbl= pd.concat([mis_val, mis_valPercent, miss_val_dtype], axis=1)

#Rename the columuns
miss_val_table_ren_columuns= mis_valTbl.rename(columuns = {0: 'Missing Values' . 1:  % of Total Values', 2: 'Dtype'})

#sort the table by percentage of missing 

miss_val_table_ren_columuns = miss_val_table_ren_columuns[
   miss_val_table_ren_columuns.iloc[:, 1] !=0].sort_values(
   '% of Total Values', ascending=False).round(1)

#Print sumary
print("You selected dataframe has " + str(df.shape[1]) + "columns. \n"
      "There are " + str(miss_val_table_ren_columuns.shape[0]) +
      " columns that have missing values.")

# Return the dataframe with missing information
return miss_val_table_ren_columuns 

