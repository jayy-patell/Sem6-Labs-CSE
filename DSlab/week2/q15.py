import pandas as pd

df1_data = {
    "Name": ["Akarsh", "Yuvraj", "Jay"]
}
df1 = pd.DataFrame(df1_data)

# Create df2 with four columns 'Maths', 'Physics', 'Chemistry', and 'Biology'
df2_data = {
    'Maths': [85, 9, 78],
    'Physics': [92, 38, 75],
    'Chemistry': [89, 34, 80],
    'Biology': [78, 77, 87]
}
df2 = pd.DataFrame(df2_data)

# Concatenate df1 and df2
df_new = pd.concat([df1, df2], axis = 1)

# Insert a new column 'Total' and calculate the sum of all marks
df_new["Total"] = df_new['Maths'] +  df_new['Physics'] + df_new['Chemistry'] + df_new['Biology']

print("Concatenated DataFrame df_new:")
print(df_new)
