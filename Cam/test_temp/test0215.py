a = '1"'
b = "1/3200"
bb = b.split('/')
b1 = float(bb[0])
b2 = float(bb[1])
b = b1/b2


print(bb)
print(b)
# b = str(b)
print(a.endswith('"'))

a = "1\""
print(a)
print(a.endswith("\""))

if a.endswith("\""):
   a = a[:-1]
print(a)
a = float(a)
b = float(b)

if a> b:
    print("True")
else:
    print("False")