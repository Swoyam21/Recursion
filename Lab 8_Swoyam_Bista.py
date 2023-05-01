# initialize empty lists and dictionary
items = []
prices = []
grocery_dict = {}

# loop until the user enters 'DONE'
while True:
    item = input("Enter grocery item or 'DONE' to finish: ")
    if item.lower() == "done":
        break
    price = float(input("Enter price: "))
    # append item and price to respective lists and dictionary
    items.append(item)
    prices.append(price)
    grocery_dict[item] = price

# print grocery list, prices, grocery dictionary, and total cost
print("Grocery List: ", items)
print("Prices: ", prices)
print("Grocery Dictionary: ", grocery_dict)
print("Total: ", sum(prices))


def compare_purchases(purchase1, purchase2):
    if purchase1 == purchase2:
        return True
    else:
        return False


def print_purchase_difference(purchase1, purchase2):
    # compare two purchases and print the price difference for each item
    for item in purchase1:
        if item in purchase2:
            if purchase1[item] != purchase2[item]:
                if purchase1[item] > purchase2[item]:
                    print(item + " is cheaper on purchase2.")
                else:
                    print(item + " is cheaper on purchase1.")
            else:
                print(item + " has the same price on both purchases.")
        else:
            print(item + " is only on purchase1.")

    for item in purchase2:
        if item not in purchase1:
            print(item + " is only on purchase2.")

# initialize an empty dictionary for grocery purchase
grocery_purchase_dict = {}

# loop until the user enters 'DONE'
while True:
    item = input("Enter new item or 'DONE' to finish: ")
    if item.lower() == "done":
        break
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    # add item, quantity, and price to grocery purchase dictionary
    grocery_purchase_dict[item] = {'quantity': quantity, 'price': price}

# print the purchase details for each item in grocery purchase dictionary
for item in grocery_purchase_dict:
    qty = grocery_purchase_dict[item]['quantity']
    price = grocery_purchase_dict[item]['price']
    if qty == 1:
        print("Purchase 1", item, "at price", price, "dollar each.")
    else:
        print("Purchase", qty, item + 's', "at price", price, "dollars each.")
