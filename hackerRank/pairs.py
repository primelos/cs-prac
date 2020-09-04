# You will be given an array of integers and a target value. Determine the number 
# of pairs of array elements that have a difference equal to a target value.

# For example, given an array of [1, 2, 3, 4] and a target value of 1, 
# we have three values meeting the condition: 2 - 1 = 1, 3 - 2 = 1 , and 4 - 3 = 1 

def pairs(k, arr):

    counter = 0
    arr_set = set(arr)
    for val in arr:
        if val - k in arr_set:
            counter += 1
    return counter



print(pairs(1, [1,2,3,4]))