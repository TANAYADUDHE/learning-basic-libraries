import pandas as pd

#create a simple dataframe
data={
    'Name':["Alice",'Bob','Charlie','Tanaya','Arohi'],
    'Age':[25,30,35,21,22],
    'City':['New York','Paris','London','Yavatmal','Nagpur'],
    'College':['COEP','VNIT','GCOA','YCC','JDIET']

}
df=pd.DataFrame(data)

#display the dataframe
print(df)
#access a column
print(df['Name'])
#basic statistics
print(df['Age'].mean()) #average age
#filter rows
print(df[df['Age']>25])