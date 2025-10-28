myset = {1,2,1,3,2,1,4,4,5,5}
print("set :", myset)

myset.add(5)
print("updated set:" , myset)

set1 = myset
set2 = {2,4,6,}

print("\nset 1" , set1)
print("set2", set2)

print("difference")
difference = set2.difference(set1)
print(difference)

print("symetric difference")
syetric = set1.symmetric_difference(set2)
print(syetric)