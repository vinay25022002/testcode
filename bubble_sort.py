def bub_sort(l):
    n = len(l)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


list1 = [64, 34, 25, 12, 22, 11, 90]

print("Original List: ", list1)
    
bub_sort(list1)
    
print("Sorted List: ", list1)
