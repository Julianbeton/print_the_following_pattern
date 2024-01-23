# Exercise 8: Print the following pattern

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

for number in range(6):
    for pattern in range(number):
        print("\033[1;32;40m", number, end = " ")

    print("\n")