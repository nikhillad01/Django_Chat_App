def demo(n):

    if n==1:
        return 1
    else:
        return  (n*demo(n-1))
l=[1,2,3,5,7,4,26,40]
print(sorted(l))


print(demo(5))
