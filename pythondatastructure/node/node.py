class daynames:
    def __init__(self, dataval: object = None) -> object:
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Tue')
e3 = daynames('Wed')

e1.nextval = e3
e3.nextval = e2

# Traversing
print(e1.dataval)
print(e1.nextval.dataval)
print(e1.nextval.nextval.dataval)

