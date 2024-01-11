import pandas as pd

data = {
    'Name': ['Akarsh', 'Yuvraj', 'Jay'],
    'Quiz_1/10': [8, 6, 9],
    'In-Sem_1/15': [12, 7, 11],
    'Quiz_2/10': [7, 7, 7],
    'In-Sem_2/15': [13, 10, 12]
}
df = pd.DataFrame(data)

# Insert a new column 'Total' and calculate the sum of all marks
df['Total'] = df['Quiz_1/10'] + df['In-Sem_1/15'] + df['Quiz_2/10'] + df['In-Sem_2/15']

# Calculate the mean for all columns
mean_all_columns = df.drop('Name', axis=1).mean()

# Add a new row with mean values
df.loc['Mean'] = mean_all_columns

print("Updated DataFrame:")
print(df)
