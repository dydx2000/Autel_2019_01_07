items = [8, 23, 45,'goulun']
y = iter(items)
z=next(y)
print(z)
print(z)
print(z)



'''
for index in range(len(items)):
    print(index, "-->", items[index])'''

'''for index, item in enumerate(items,start =2):
    print(index, "-->", item)'''

dic1 ={'a':1,'b':2,'c':3,'d':4,'e':5,'for':'what'}

for index,item in enumerate(dic1):
    print(index,'-->',item,)

print(next(iter(dic1)))
print(next(iter(dic1)))
print(next(iter(dic1)))
items = [8, 23, 45,'goulun']

while items:
    print(items)
    items.pop()