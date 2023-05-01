
# def new_print(func):

#     def wrapper():
#         print("EXTRA LINE")
#         return func()
#     return wrapper

# @new_print
# def display_func():
#     print("display line")
    
# display_func()


# question 21
# open_f = open("demofile2.txt", "a")
# open_f.write("Now the file has more content!")
# open_f.close()



# question 22
# name_dict = {}
# open_f = open("C:/Users/Learner_9ZH3Z126/Downloads/nameslist.txt", 'r')
# res = open_f.read().split()


# for words in res:
#     name_dict[words] = res.count(words)

# print(name_dict)

# question 23
# open_prime = open("C:/Users/Learner_9ZH3Z126/Downloads/primenumbers.txt", "r")
# split_prime = open_prime.read().strip().split()

# open_happy = open("C:/Users/Learner_9ZH3Z126/Downloads/happynumbers.txt", "r")
# split_happy = open_happy.read().strip().split()

# for i in split_prime:
#     if i in split_happy(i):
#         print(i, end=" ")

#question 24
board_game_size = int(input("Enter a number"))
print(board_game_size)
for i in range(board_game_size):
    print(' ')
    print(" --- " * board_game_size)
    print(' ')
    for j in range(board_game_size+1):
        print("|   ", end=" ")
    print()
print(" --- " * board_game_size)




#question 25








