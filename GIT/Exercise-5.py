#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).

a = set([1,2,3,4,5,6,7,8,9,1,2,3])

b = set([2,3,4,5,6,7,8,1,1,13,4,5])

print list(a.intersection(b))


