import pandas as pd

# READ CSV FILE *******
# df = pd.read_csv('./datafile/sales_data_sample.csv',encoding='latin1')
### df = pd.read_csv('./datafile/sales_data_sample.csv',encoding='latin1 OR utf-8') # error throw not read csv file and encode error and write to use
# print(df)
 
### read excel file
# df = pd.read_excel('./SampleSuperstore.xlsx',engine='openpyxl')
# print(df)

### read csv file
# df = pd.read_csv('./datafile/Output1.csv')
# print(df)

### create serise
# serise = pd .Series([10,20,30,40])
# print(serise) # print index and value 

# serise = pd.Series([1,2,3,4],index=['a','b','c','d']) # customize index create
# print(serise)


### use index and access value using index
# print(serise['a'])
# print(serise['d'])


### Create Series from a dictionary:
# dicSe = {'name':'bhavin','age':21,'number':9090909090}
# var = pd.Series(dicSe)
# print(var)

### Create Series from a dictionary and use to index
# dicSe = {'name':'bhavin','age':21,'number':9090909090}
# var = pd.Series(dicSe,index=['name','age','number']) # use to index is same to use in dict 
# print(var)


### create data frames
data = {
    "name":["Bhavin","Anand","Sagar","Raj"],
    "Age":[43,54,23,34]
}

# df = pd.DataFrame(data)
# print(df)
# print(df.loc[0]) # select single index
# print(df.loc[[0,1]]) # select mutiple index

# print(df.iloc[0])

## loc and iloc
# df = pd.DataFrame(data,index=['a','b','c','d'])
# print(df)
# print(df.iloc[0]) # iloc is return to specific row's but allow to in index base
# print(df.loc['a']) # loc is use and return specific row's and use to index name and index like ('name' and 0)
# print(df.loc[['a','b']]) # loc multiple use  index and return specific row's

### read csv file and name index create
# df = pd.read_csv('./datafile/Output1.csv',index_col='Name')
# print(df.loc['Ram'])
# print(df.iloc[1])
# print(df.to_string())

