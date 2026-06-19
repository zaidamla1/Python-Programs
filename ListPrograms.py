# Remove Duplicates Without Using set()
lst1 = [1, 2, 3, 2, 4, 1, 5]
result = []

for i in lst1:
    if i not in result:
        result.append(i)

print(result)



# Find Second Largest Element
lst2 = [10, 20, 4, 45, 99]
largest = second = float('-inf')

for num in lst2:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)


# Rotate List by K Positions
lst3 = [1, 2, 3, 4, 5]
k = 2

k = k % len(lst3) #2

rotated = lst3[-k:] + lst3[:-k]   # [4,5] + [1,2,3]
print(rotated)

# Find All Pairs With Given Sum
lst4 = [2, 4, 3, 5, 7, 8, 9]
target = 7

for i in range(len(lst4)):
    for j in range(i+1, len(lst4)):
        if lst4[i] + lst4[j] == target:
            print(lst4[i], lst4[j])




# Flatten a Nested List
nested = [[1,2], [3,4], [5]]
flat = []

for sub in nested:
    for item in sub:
        flat.append(item)

print(flat)