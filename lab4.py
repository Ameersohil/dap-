import pandas as pd
import numpy as np
from numpy import nan as NA
data=pd.read_csv('ex1.csv')
print (data)
print(50*'-')
print("data is null")
print(data.isnull())
print(50*'-')
print("drop na")
print(data.dropna())
print(50*'-')
print("fillna returns a new object, but you can modify the existing obj")
print("fill na with 0")
_=data.fillna(0,inplace=True)
print(data)
print(50*'-')
print("each row is a duplicate?")
print(data.duplicated())
print(50*'-')
print('drop duplicate')
print(data.drop_duplicates())
print(50*'-')
print('drop duplicate')
print(data.drop_duplicates(['something']))
print(50*'-')
print('replace -999 eith NA values')
print(data.replace(-999, np.nan))
print(50*'-')
print('detecting and filtering outliers')
data=pd.DataFrame(np.random.randn(1000,4))
print(data.describe())
print(50*'-')
print('select all rows having a value exceeding 3 or -3')
print(data[(np.abs(data)>3).any(1)])
print(50*'-')
print('cap values outside the interval -3 to 3')
print("the statement np.sign(data) produces 1 and -1 values based on whether the values in data are positive or negative")
data[np.abs(data)>3]=(np.sign(data)*3)     
print(data.describe())