dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

#Updating
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

for x in dict:
    print(x)

# Delete Dictionary Elements
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict1['Name']; # remove entry with key 'Name'
dict1.clear();     # remove all entries in dict
del dict1 ;        # delete entire dictionary

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
