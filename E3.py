import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

data = 'output.csv'
df = pd.read_csv(data)

print('\n1) View dimensions of dataset')
print(df.shape)


print('\n2) Review the dataset')
print(df.head())

print('\n3) View summary of dataset')
print(df.info())

print('\n4) Check for missing values')
print(df.isnull().sum())

print('\n5) Descriptive statistics with describe() function')
print(df.describe())

print('\n6) Summary statistics of character columns')
print(df.describe(include=['object']))

print('\n7) Summary statistics of all the columns')
print(df.describe(include='all'))
