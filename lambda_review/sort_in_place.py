def sort_in_place(arr):
    print(len(arr))
    for item in range(1, len(arr)):
        
        current = arr[item]
        j = item - 1
        print(j)
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        print(j)
        arr[j+1] = current
    return arr






arr = [1,0,0,1,2,0,1,2,0,1]
print(sort_in_place(arr))