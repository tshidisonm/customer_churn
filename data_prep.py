import pandas as pd

#loading the dataset
df = pd.read_csv('data.csv')


#checking for missing values
print(df.isnull().sum())