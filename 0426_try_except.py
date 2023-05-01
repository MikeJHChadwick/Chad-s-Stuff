
# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was {}'.format(x)) #checks if a condition is false and throws


# assert x >= 5, 'x should not exceed 5. The value of x was {}'.format(x) #checks if a condition is met and if true continue


def sum(num1, num2):
    total= num1 + num2
    return total

answer = sum(2,2)
#print(answer)

def modify_x():
    assert x <= 5, 'x should not exceed 5. The value of x was {}'.format(x)
    print('x is being modified')

"""
try: 
    x = 50
    modify_x()
except AssertionError as error:
    print(error)
    print('modify_x() function was not successfully executed')
"""


try:
    x = 10
    modify_x()
    f= open('my_file.txt')
except FileNotFoundError as fnf_error:
    print(fnf_error)
    print('file does not exist')
except AssertionError as error:
    print(error)
    print('modify_x() function was not successfully executed')
else:
    print('everything looking good')
finally: 
    print('We did it!')