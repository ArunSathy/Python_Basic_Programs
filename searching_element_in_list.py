li=[1,2,3,4,5]

n=int(input('Enter the element to find : '))

# first way -----

# count=0
#
# for i in li:
#     if n==i:
#         count=1
#         break
# if count==1:
#     print('Present')
# else:
#     print('Absent')

# second way -----

if n in li:
    print('Present')
else:
    print('Absent')