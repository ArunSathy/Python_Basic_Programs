string='Arun Sathyan'

# first way using for() -----

# count=0
#
# for i in string:
#     count+=1
# print('first way : ',count)

# second way using while & slicing -----

# count=0
#
# while string[count:]:
#     count+=1
# print('second way : ',count)

# third way using len() -----

# print('third way : ',len(string))

# fourth way using join and count -----

text='_'

print('fourth way : ',text.join(string).count(text)+1) 

