Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)

for d in Days:
	print(d)

# #Adding Items to a Set
Days.add("Sun")
print(Days)
# Removing Item from a Set
Days.discard("Sun")
print(Days)
#
# Union
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)
#
# Intersection of Sets
AllDays = DaysA & DaysB
print(AllDays)
#
# Difference of Sets
AllDays = DaysA - DaysB
print(AllDays)
#
# Compare Sets
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)
