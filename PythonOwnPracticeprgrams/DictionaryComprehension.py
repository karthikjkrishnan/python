#Converting list of tuples into dictionary
list1=[('a',5),('b',10),('c',11)]
dict_converting = {k:v for k,v in list1}
print dict_converting

#Alter method uisng dict keyword
dict_converting= dict(list1)
print dict_converting
