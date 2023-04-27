import pandas as pd
import networkx as nx
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("facebook.csv")
print(df.head())

import warnings
warnings.filterwarnings("ignore")

print("\n1. Find Null Values\n")
print(df.isnull().sum())
print(df)

missing_value = ["N/A", "na", np.nan]
df = pd.read_csv("facebook.csv", na_values=missing_value)

print(df.isnull().sum())

print("\n2. Show Heatmap presentation\n")
sns.heatmap(df.isnull())
plt.show()

print("\n3. Fill null values by 0\n")
df1 = df.fillna(0)
print(df1)

print("\n4. Fill null values by particular values\n")
df1 = df.fillna(1)
print(df1)

print("\n5. Fill null values by forward fill method\n")
dfl = df.fillna(method="ffill")
print(dfl)

print("\n6. Fill null values by backward fill method\n")
dfl = df.fillna(method="bfill")
print(dfl)

print("\n7. Fill null values by interpolation\n")
dfl = df.interpolate()
print(dfl)

print("\n8. Drop null value\n")
dfl = df.dropna()
print(dfl)

print("\n9. Drop null values only if entire row is null\n")
dfl = df.dropna(how="all")
print(dfl)

print(dfl.shape)
print("\n10. Drop duplicate values\n")
dfl = df.drop_duplicates()
print(dfl.shape)