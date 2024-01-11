# # Introduction to PANDAS
import pandas as pd
import numpy as np
# s=pd.Series([3,9,-2,10,5])
# print(s.sum())
# print(s.min())
# print(s.max())

# # Creating a Data Frame
# import pandas as pd
# data = [['Dinesh',10],['Nithya',12],['Raji',13]]
# df = pd.DataFrame(data,columns=['Name','Age'])
# print(df)

# # Indexed Data Frame
# data = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
# print(df)

# # Creating a DataFrame using Dictionary
# df1=pd.DataFrame({'A':pd.Timestamp('20130102'),'B':np.array([3]*4,dtype='int32'),'C':pd.Categorical(['Male','Female','Male','Female'])})
# print(df1.shape)
# print(df1.dtypes)
# print(df1.head())  #will display first 5 records
# print(df1.tail())  #will display last 5 records
# print(df1.describe())
# print(df1.T)  # will transpose the data frame

# EG
dates=pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100,4), index=dates, columns=list('ABCD'))

# print(df.head())  #To view first 5 records
# print(df.tail())  #To view last 5 records
# print(df.index)  #To view the index
# print(df.columns)   #To view the column names
# print(df.T)  #To transpose the df
# print(df.sort_index(axis=1,ascending=False))  #Sorting by Axis
# print(df.sort_values(by='B'))  #Sorting by Values
# print(df[0:3])  #Slicing the rows
# print(df['20130105':'20130110'])  #Slicing with index name

# #Slicing with row and column index (like 2D Matrix)
# print(df.iloc[0])  #will fetch entire 1st row
# print(df.iloc[0,:2])  #will fetch 1st row, first 2 columns
# print(df.iloc[0,0])  #will fetch 1st row, 1st column element (single element)
# print(df['A'])  #Selecting a single column
# print(df[['A','B']])  #Selecting more than one column
# print(df[['A','B']][:5])  #Selecting more than one column, with selected number of records
# print(df.loc['20130101':'20130105',['A','B']][:5])  #Selecting more than one column, with selected number of records


# # Boolean Indexing
# df[df.A>0]  #will fetch all positive values of A column
# #Include a 6th column (a categorical) character data
# df['F']=['Male','Female','Female','Male','Female','Female']
# #Setting by assigning with a numpy array
# df.loc[:,'D']=np.array([5]*len(df))  #Which will replace the ‘D’, column with all 5

# # Deleting a row or column
# df.drop ('A', axis =1, inplace=True)
# df.drop ('20130406', axis =0, inplace=True)
# print(df)


# # Concatenation of two Data Frames
# df1 = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Age':[28,34,29,42]}
# df2 = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Age':[28,34,29,42]}
# Df_new= pd.concat (df1, df2, axis=1)