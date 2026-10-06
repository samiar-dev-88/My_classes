import pandas as pd

dic = {
    "Name" : ["ali" , "houman" , "elena"],
    "Age" : [8 , 12 , 16],
    "Class" : [202 , 202 , 604],
    "Class Time" : ["Sunday" , "Thursday" , "Monday"],
    "Clock" : ["20:00" , "8:00" , "6:00"]
}
a = pd.Series(["ali" , "houman" , "elena"] , index=[10 , 3 , 5])
b = pd.DataFrame(dic)
print(b)

print(b.head())
print(b.tail())
print(b.columns)

print(b["Age"].max())
print(b["Class"].sum())