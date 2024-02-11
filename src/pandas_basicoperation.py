import pandas as pd

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