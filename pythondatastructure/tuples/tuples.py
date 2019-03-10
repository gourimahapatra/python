tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
tup4=()
tup5 = ((56,67,))
print(tup4)
#Accessing Tuple element

print(tup1[0])
print(tup1[0:3])

#updating tuple

#Tuples are immutable which means you cannot update or change the values of tuple elements. You are able to take portions of existing tuples to create new tuples

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
tup3 = tup1+ tup2
print(tup3)

#Delete Tuple Elements
#Removing individual tuple elements is not possible because its immuatable
#we can put element and delete parent one
tup = ('physics', 'chemistry', 1997, 2000);
print(tup);
# del tup;
print ("After deleting tup : ");
print (tup);

# Basic Tuples Operations
len(tup1)
print(tup1 + tup2)
print(tup1 * 4)
print(1997 in tup1)
for x in tup1:
    print(x)

