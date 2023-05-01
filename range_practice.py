# def sequence(low, high):
#     for x in range(low,high):
#         for y in range(high,low-1,-1):
#             if y == low:
#                 print(str(y))
#             else:
#                 print(str(y), end=", ")

# sequence(1,3)

# for x in range(1,10,3):
#     print(x)


# for x in range(10):
#     for y in range(x):
#         print(y)

num1 = 0
num2 = 0

for x in range(5):
    for y in range(14):
        num2 = y + 3

print(num1 + num2)