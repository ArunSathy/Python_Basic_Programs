li=[1,2,3,4,1,5,6,1,7,8,1]
# find how many 1's are in the list
print('My list : ',li)

# first way using count() -----

# print('first way : ',li.count(1))

# second way using for() -----

# count=0
#
# for i in li:
#     if i==1:
#         count+=1
# print('second way : 1 has occured {} times'.format(count))


# third way using counter() -----

from collections import Counter

x=Counter(li)  # will return count of every element in the list in a dictionary, it's a dictionary function

print('third way : ',x[1])
