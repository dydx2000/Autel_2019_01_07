a = [1,2,3,4,6,8]
b =iter(a)
i = next(b)
print('next:',i)
l = next(b)
# print('next is:',l)
# print('next is:',)
print('next is:',next(b))
print('next is:',b.__next__())
print('next is:',b.__next__())
print('next is:',b.__next__())

list = [1,34,394,4,3,4,32,32,343,44,3,78,7,43,4,45,6]
b = iter(list)
try:
    while True:

        i= next(b)
        print("next: ",i,end='  ')
except StopIteration:
    # print('\n已经迭代完了.')
    pass
# for x in reversed(a):
#     print(x)
#
# a = 'dadashazhu cai'
# print(a[None:-2])