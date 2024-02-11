import pandas as pd
import numpy as np
'''
in this we will be learnig about the 
pandas library functions
'''

#now lets create the series in pandas
'''
series is the list of indexed values, having multiple features
'''
#series using list
myList = [1,2,3,4,5,6,7,8,9,0]
pandasSeries = pd.Series(myList)
print(pandasSeries)

#now lets check the type of series
print('type of the series:',type(pandasSeries)) # here the dtype will be int as we have passed int values

#now lets create the empty series
emptySeries = pd.Series([])
print('empty series:',emptySeries)
print('type of empty series:',type(emptySeries)) #observe here the dtype will be float as it is default -->going to be object in coming versions

#now lets create the series with user defined index and name it to roman index series
userDefinedIndex = pd.Series(['A','B','C','D'],index = ['I','II','III','IV'],name ='roman index')
print('user defined series:\n',userDefinedIndex)

#scalar series
scalarSeries = pd.Series(1)
print('scalarSeries:\n',scalarSeries)
print('post increase of index:\n',pd.Series(1,index=[0,1,2,3]))

'''
creating the series using dictionaries
'''
my_info = {'name':'uday','id':1252,'location':'us'}
dictSeries = pd.Series(my_info)
print('dictSeries:\n',dictSeries)

#multi dimentioanl series with dict
user_def_dict = {'p':[1,2,3],'q':[2,4,6],'r':[2,3,5],'s':[2,6,8.9]}
user_def_dict_ser = pd.Series(user_def_dict)
print('user_def_dict_ser:\n',user_def_dict_ser)

#accessing the data
print(user_def_dict_ser[0])
print(user_def_dict_ser[max(user_def_dict)])


'''
now lets understand the dataframe
'''
#dataframe using list
dataFrameList = [1,2,4,5,6,7,8]
dataFrame =pd.DataFrame(dataFrameList)
print('dataframe :\n',dataFrame)

#dataframe with multiple list
multiListDataFrame = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,0]])
print('multi list dataframe:\n',multiListDataFrame)

#dateframe using dict
dictDataFrame = pd.DataFrame(user_def_dict)
print('dict dataframe:\n',dictDataFrame)

'''
reading the csv file using read_csv()
skipfooter=1 --> will skip the foot by 1, used when we dont need the footer
'''
uberDataFrame = pd.read_csv('dataset/UberDataset.csv',skipfooter=1)

#to get the columns of the dataframe
print('columns:',uberDataFrame.columns)
#to get the size of the dataframe
print('size of the dataframe:',uberDataFrame.size)

#shape of the dataframe (rows, columns)
print('shape of the dataframe',uberDataFrame.shape)
print('rows:',uberDataFrame.shape[0])
print('colms:',uberDataFrame.shape[1])

#to get to know the info of the dataframe--> will give the overall information
#will give the non-null info and datatype
print('uber data information:\n',uberDataFrame.info())

#describe() function to get the stats of only numeric colmns
print('uber data description:\n',uberDataFrame.describe())
#describe(include='all') will give stats for all colms
print('uber data description All:\n',uberDataFrame.describe(include='all'))

#get the head --> default is 5
print('default head:\n',uberDataFrame.head())

#custom head
print('custom head:\n',uberDataFrame.head(20))

#get the tail --> default is 5
print('default tail:\n',uberDataFrame.tail())

#custom tail
print('custom tail:\n',uberDataFrame.tail(20))

'''
now lets study about the null values, how to check null values
and how to replace the null values, it always advisable to not to
drop the missing values as it could lead to possible matrix loss.
'''
#to check the if any null values in the dataframe
print('is na boolean metrix:\n',uberDataFrame.isnull())

#now lets find by each column
print('each colmns nulls:\n',uberDataFrame.isnull().sum()) #after running this you will find purpose having nulls

#now lets get the complete null values in the dataframe
print('all null values in the dataframe:',uberDataFrame.isnull().sum().sum())

'''
now lets remove the null values
'''
modified_df1 = uberDataFrame.dropna() #default axis=0 it means rows with null will be removed
print('shape before removing rows with the null values:',uberDataFrame.shape)
print('shape after removing rows with the null values:',modified_df1.shape)

#now if i want to delete the columns with the null values
modified_df2 = uberDataFrame.dropna(axis=1) #here the columns with the null will be droped
print('shape before removing rows with the null values:',uberDataFrame.shape)
print('shape after removing rows with the null values:',modified_df2.shape)

#now if i want to delete the rows having any null values
modified_df3 = uberDataFrame.dropna(how='any')
print('shape before removing rows with the null values:',uberDataFrame.shape)
print('shape after removing rows with the null values:',modified_df3.shape)

#now if i want to delete the rows having all null values
modified_df4 = uberDataFrame.dropna(how='all')
print('shape before removing rows with the null values:',uberDataFrame.shape)
print('shape after removing rows with the null values:',modified_df4.shape)

#now if i want to change the orginal dataframe after removing the null's
#use inplace= True
uberDataFrame.dropna(inplace=True)
print('after in place orginal dataframe shape:',uberDataFrame.shape)

'''
now lets understand the filling the null values, to avoid the matrix loss by dropping
'''
print(np.char.center(' Filling the NA ',100,'*'))
uberDataFrame = pd.read_csv('dataset/UberDataset.csv',skipfooter=1)

#checking the null values
print('checking null values:',uberDataFrame.isnull().sum())

'''
it is always advised to fill the Na with mean or median
mean --> it could change the scew of the graph and outliers can manipulate the outcome
median --> it wont impact the scew and impact is less on outcome
for categorical it is advised to replace with mode(freq)
'''
#in our senario we have PURPOSE as null, which is of type object
#hence we need to replace with the mode
print('mode:',uberDataFrame['PURPOSE'].mode().values[0])

uberDataFrame.fillna(uberDataFrame['PURPOSE'].mode().values[0],inplace=True)
print('checking null values post fillNa:',uberDataFrame.isnull().sum())

#comment the above two lines to test the below method.
#this can also be achived by using dict
uberDataFrame.fillna({'PURPOSE':uberDataFrame['PURPOSE'].mode().values[0]},inplace=True)
print('checking null values post fillNa:',uberDataFrame.isnull().sum())

'''
other method are forward fill and backward fill
'''
print(np.char.center(' Filling the NA using ffill and bfill',100,'*'))
uberDataFrame = pd.read_csv('dataset/UberDataset.csv',skipfooter=1)
#forward fill
'''
fills the null values with the prev - value 
if row - 10 is MEETING and row - 11 is null
now the 11 row will be filled with value of 10 row
'''
uberDataFrame.fillna(method='ffill') #default is axis = 0

#backward fill
'''
fills the null values with the next - value 
if row - 12 is MEETING and row - 11 is null
now the 11 row will be filled with value of 12 row
'''
uberDataFrame.fillna(method='bfill')

#if we make axis=1 the concept will become vis-ver-sa
#forward fill
'''
fills the null values with the prev - value 
if row - 10 is MEETING and row - 11 is null
now the 11 row will be filled with value of 10 col
'''
uberDataFrame.fillna(method='ffill',axis=1)
#backward fill
'''
fills the null values with the next - value 
if row - 12 is MEETING and row - 11 is null
now the 11 row will be filled with value of 12 col
'''
uberDataFrame.fillna(method='bfill',axis=1)