# Repeating code: Functions

# 4 Built-in Functions that have been used before on the course:
print("Hello New World!") #print() writes on the terminal an inserted data
user_input = input("Enter a number: ") #input() requests an input from the user, which is set as a string ""
user_number = int(user_input) #int() turns the argument (like a string) into an int data type
range_list = range(10) #range() makes a list from 0 to a set number
print(range_list)

# 2 New Function
List = ["Horse", "Rabbit", "Human", "Crocodile", "wolf", "Animal", "Bucket", "Bird", "Eagel", "Cat", "Dog", "Mouse", "Fox", "Frog", "House"]
NewList = zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], List) # zip(), produces a tuple between two items

for i in NewList:
    print(i)
