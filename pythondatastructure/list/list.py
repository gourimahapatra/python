list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];
list2[2] = 2001;
del list1[0];
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print(len([3,4]))
print(len(list1))
print([3,4,5]+[5,6,"sdas"])
print(['Hi']*5)
print(3 in [4,5,6,7,3])

for x in list2:
    print(x)
