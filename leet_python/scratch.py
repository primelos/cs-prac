# try things here


def test1(a,b):
    while a != 0 and b != 0:
        print('one')
        if a:
            a -=1
            print(a)
        print('two')
        if b:
            b -=1
            print(b)
        



a= 5
b= 5
print(test1(a,b))


def invert(b):
    if b is None:
        return 

    invert(b.left)
    invert(b.right)
    b.left, b.right = b.left, b.right

    return b