li=[1,5,3,6,4,2]
# finding the second largest element in a list

# first way using sort() -----

# li.sort()
#
# print('first way : ',li[-2])

# second way -----

# li.sort()
# li.pop(-1)
#
# print('second way : ',li[-1])

# third way using remove() -----

li.remove(max(li))

print('third way : ',max(li))