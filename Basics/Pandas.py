import pandas

list = pandas.read_csv('./list.csv')
#print(type(list))

list1 = pandas.DataFrame({'A':[1,2,3], 'b':[5,6,7]})
list1.to_csv('./list1.csv')

list2 = pandas.concat([list, list1], sort = True)
list2.to_csv('./list2.csv')
list3 = pandas.read_csv('./list3.csv')

#print(list.columns[0])

print(list2.loc[0])
print("**********")
print(list3.iloc[0,0])