from array import *

array1 = array('i', [12, 23, 34, 56, 65, 54, 43, 22, 22])

print(array1[0])

array1.insert(0, 100)
array1.remove(22)

array1[7] = 567
y = 0
for x in array1:
    # y = y + x
    # print(y)
    print(x)
