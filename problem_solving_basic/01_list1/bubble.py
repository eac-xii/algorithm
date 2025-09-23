def bubble_sort(a, N):
    for i in range(N - 1, 0 , -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
                
arr = [9, 2, 3, 8, 2, 4]
n = 6
sorted_arr = bubble_sort(arr, n)
print(sorted_arr)