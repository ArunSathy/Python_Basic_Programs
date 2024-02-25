# find the maximum and minimum element

ar=[110,999,232,235,185,109]

# print(max(ar))
# print(min(ar))

max=ar[0]

for i in range(len(ar)):
    if ar[i]>max:
        max=ar[i]
print(max)

min=ar[0]

for i in range(len(ar)):
    if ar[i]<min:
        min=ar[i]
print(min)