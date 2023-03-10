lst = [1, 5, 3, 2, 8, 9, 6, 4, 7]
print(lst)

for i in range(len(lst)):
    index = i
    for j in range(i + 1, len(lst)):
        if (lst[index] > lst[j]):
            index = j
    lst[i], lst[index] = lst[index], lst[i]
    
print(lst)