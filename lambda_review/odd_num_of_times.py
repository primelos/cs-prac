def get_odd_occurances(arr, arr_len):
    # SLOWER
    # for i in range(arr_len):
    #     count = 0
    #     for j in range(arr_len):
    #         if arr[i] == arr[j]:
    #             count +=1
    #     print('count',count)
    #     if count % 2 != 0:
    #         return arr[i]
    # return -1

    # FASTER
    hash = {}
    for i in range(arr_len):
        if arr[i] not in hash:
            hash[arr[i]] = 0
        hash[arr[i]] += 1

    for j in hash:
        if hash[j] % 2 != 0:
            return j
    return -1





arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2, 4 ] 
n = len(arr)
print(get_odd_occurances(arr, n))

