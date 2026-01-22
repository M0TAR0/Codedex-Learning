menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]

def welcome():
    j = 1
    print("Welcome! Here's the menu")
    for i in menu:
        print(j, "-", i)
        j += 1

def get_item(x):
    item = menu[x-1]
    return item

welcome()

selected_item = int(input("Please enter the number of the item you want: "))

print("Here! This is your order: ", get_item(selected_item))