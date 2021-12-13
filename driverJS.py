from shoppingListJS import ShoppingJS
# function for prompting list of products purchased 
def purchases():
    # number of items
    num = 0

    # list of items 
    li = []

    # validation of input for number of items 
    while num < 1:
        num = int(input("How many items will you order today? "))
        if num < 1:
            print("number of items must be at least 1")

    for i in range(num):
        print("item #", i + 1)
        food = input("Enter food: ")
        # validation for amount entered
        while amount <= 0:
            print ("amount must be greater than 0")
            amount = eval(input("Enter amount of pounds: "))
        print()
        li.append(ShoppingJS(food, amount))
        return li

# function for displaying products purchased 
def display(itemList):
    print("here's a summary of the items purchased: ")
    print("-----------------------------------------")
    for shoppingJS in itemList:
        print(f"Item: {shoppingJS.getFood()}")
        print(f"Amount: {shoppingJS.getAmount()}") 
        print(f"Price per pound: {shoppingJS.getUnitPrice():.2f}")
        print(f"Price of order: {shoppingJS.getNetPrice():.2f}")

# function for total price
def totalPrice(itemList):
    total = 0
    for i in itemList:
        total += i.getNetPrice()
    print ("Total: ${:.2f}".format(total))


# main function calling other functions 
def main():
    itemList = purchases()
    display(itemList)
    totalPrice(itemList)


# calling main function
    main()