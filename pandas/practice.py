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
# data = {
#     "name":["Bhavin","Anand","Sagar","Raj"],
#     "Age":[43,54,23,34]
# }

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


# df = pd.read_csv('./datafile/movieRecords.csv')
# print(df)
# print(df.head(1))
# print(df.tail())
# print(df.info())

# print(df.describe()) 
# print(df.shape) # return shape of dataframe
# print(df.dtypes) # return data type of column 
# print(df.ndim) # return dimension of dataframe
# print(df.size) # return it's size
# print(df.columns) # return column name

# print(df)
# print(df["Title"]) # select to the column 
# print(df[["Title","Director"]]) # select mutiple row's


# boolan condition use and  
# print(df[df["ReleaseYear"] > 2008])
# print(df[df["ReleaseYear"] % 2 == 0])

# mutiple condition apply  
# print(df[(df["ReleaseYear"] > 2008) & (df["ReleaseYear"] < 2014)])


# df_sales = pd.DataFrame({
#     "SaleID": [101, 102, 103, 104, 105],
#     "CustomerName": ["Ramesh", "Suresh", "Kalpesh", "Meena", "Priya"],
#     "Product": ["Laptop", "Mobile", "Headphones", "Tablet", "Smartwatch"],
#     "Quantity": [1, 2, 3, 1, 2],
#     "PricePerUnit": [55000, 15000, 2000, 25000, 5000]
# },index=['one','tow','three','four','five'])

# print(df_sales)

# print(df_sales.loc[1]) # select one row
# print(df_sales.loc[[0,1]]) # select mutiple row's

# print(df_sales.loc['one']) # select index

# df_sales['id'] = [1,2,3,4,5] # new column add and it is use and last add to column
# print(df_sales.drop(columns="id",inplace=True)) # drop() function use to delete the column 
# print(df_sales)

# print(df_sales.insert(0,"id",value=[1,2,3,4,5]))
# print(df_sales)

# df_sales.drop(columns=["id","SaleID"],inplace=True)
# print(df_sales)

# print(df_sales)
# df_sales.loc['one','SaleID'] = 111
# print(df_sales)


df_sales = pd.DataFrame({
    "SaleID": [101, 102, 103, None, 105],
    "CustomerName": ["Ramesh", "Suresh", None, "Meena", "Priya"],
    "Product": ["Laptop", "Mobile", "Headphones", "Tablet", "Smartwatch"],
    "Quantity": [1, None, 3, 1, 2],
    "PricePerUnit": [55000, 15000, None, 25000, 5000]
})

# print(df_sales)

# df_sales.dropna(inplace=True)
# print(df_sales)

# print(df_sales.isnull()) # find null value and return true in column

# df_sales.fillna('NaN',inplace=True)
# df_sales = df_sales.fillna('NaN')
# print(df_sales)

# df_sales.interpolate(method='linear',axis=0,inplace=True)
# print(df_sales)


# df = pd.Series([4,3,1,2,6])
# df = pd.read_csv('./datafile/movieRecords.csv')
# df.sort_values(ascending=True,inplace=True)
# df.sort_values(by=["MovieID","ReleaseYear"],ascending=False,inplace=True)
# print(df)


data = {
    "ProductID": [101,102,103,104,105,106,107,108,109,110],
    "ProductName": [
        "Smartphone","Laptop","Headphones","T-Shirt","Shoes",
        "Smartwatch","Tablet","Jeans","Jacket","Sandals"
    ],
    "Category": [
        "Electronics","Electronics","Accessories","Clothing","Footwear",
        "Electronics","Electronics","Clothing","Clothing","Footwear"
    ],
    "Price": [15000,55000,2000,500,1200,7000,25000,1200,3000,900],
    "Stock": [50,20,100,200,150,75,40,120,60,90],
    "Rating": [4.5,4.7,4.2,4.0,4.3,4.1,4.6,3.9,4.2,4.0],
    "Brand": [
        "Samsung","Samsung","Sony","Nike","Adidas",
        "Apple","Samsung","Puma","Puma","Bata"
    ]
}

# Create DataFrame

df = pd.DataFrame(data)
# print(df['Category'].duplicated()) # duplicate record's find and return true
# print(df)

df = pd.Series([1,2,3,1,4,5,2])
df.drop_duplicates(inplace=True) # it is use to delete duplicate recrod's
print(df.to_string())

# print(df.groupby("Category")["Price"].sum())
# print(df.groupby("Category")["Brand"].sum())
# print(df)


# df_customer = pd.DataFrame({
#     "CustomerId":[1,2,3],
#     "CustomerName":["Ramesh","Suresh","Kalpesh"]
# })
# df_oreder = pd.DataFrame({
#     "CustomerId":[2,1,4],
#     "OrderAmt":[400,899,599]
# })

# # df = pd.merge(df_customer,df_oreder,how='inner',on='CustomerId')
# # print(df)


# df = pd.concat([df_customer,df_oreder],axis=1)
# print(df)

# df = pd.concat([df_customer,df_oreder],axis=0,ignore_index=True)
# print(df)