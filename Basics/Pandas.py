import pandas

list = pandas.read_csv('./list.csv')
print(type(list))

list1 = pandas.DataFrame({'A':[1,2,3], 'b':[5,6,7]})
list1.to_csv('./list1.csv')

