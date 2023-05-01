def even_n(max_n=1):
    n = 1
    while n <= max_n:
        yield n * 2
        n+= 1

i = even_n(3)
print(next(i))
print(next(i))
print(next(i))

# a = [1,2,7,8]
# b = a[-2:]
# print(b)
# a[2:2] = [3,4,5,6] 
# print(a)