def bubble(z):
    for num in range(len(z) -1, 0, -1):
        print('num', num)
        for i in range(num):
            print('i', i)
            if z[i] > z[i + 1]:
                # 10, 9
                temp = z[i]
                z[i] = z[i + 1]
                z[i + 1] = temp
    return z
test1 = [5,88,3,14,64,2,3,9]
print(test1)
print(bubble(test1))
print(test1)
