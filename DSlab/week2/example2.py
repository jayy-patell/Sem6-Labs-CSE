# # I/O Operations with external files

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading a CSV file & XLS file format
df = pd.read_csv('business.csv')
print(df.head()) #This will display 1 st 5 records
# print(df.tail()) #This will display last 5 records
# print(df[0])
# print(df.columns)

plt.scatter(df['0'],df['1'])
plt.xlabel('0')
plt.ylabel('1')
