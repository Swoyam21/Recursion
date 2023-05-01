# Part 1 of Lab

grocerylist = []
costofItems = []

# Using while loop till the user types done in item

while True:
  item = str(input("Enter your Grocerylist Item: "))

  if item == "done":
    break    #Using break to break the while loop if the user types done
  cost = int(input("Enter the price of the grocery list items: "))
  grocerylist.append(item)          # Adding every single item in the grocerylist using .append
  costofItems.append(cost)          # Adding every single cost in the costofItems using .append

print(f"My grocer list is {grocerylist}")
print(f"My cost of the Items are {costofItems} \n")




# Part 2 of the Lab
# Converting the above two lists into dictionary in which grocerylist is the key and costofItems is the value.


#grocery = dict(zip(grocerylist,costofItems))
grocery = {grocerylist[i]:costofItems[i] for i in range(len(grocerylist))}

print(grocery)

# Part 3 of the lab
# Adding all the cost of the grocery

total_cost = 0
for i in costofItems:
  total_cost += i

print(f"Total amount spend of the grocery is {total_cost}.")


# Part 4 of the Lab
# Creating the second dictionary

new_grocery = {"apple":5,"grapes":12,"mango":12,"banana":10}

# Part 5 of the Lab

# Creating the function which have two dictionaries as the arguments to compare the prices of the items in both the dictionaries

def same_purchase(purchase1, purchase2):
    return purchase1 == purchase2



# Part 6 of the Lab

# If the purchases are different, prints the difference in items and/or prices


def diff_purchase(purchase1, purchase2):
    diff_items = set(purchase1.keys()) ^ set(purchase2.keys())
    for item in diff_items:
        if item in purchase1 and item not in purchase2:
            print(f"{item} is only in purchase1.")
        elif item in purchase2 and item not in purchase1:
            print(f"{item} is only in purchase2.")
        else:
            if purchase1[item] < purchase2[item]:
                print(f"{item} is cheaper on purchase1.")
            elif purchase1[item] > purchase2[item]:
                print(f"{item} is cheaper on purchase2.")


# Part 7 of Lab

groceryPurchase = {"banana": {"price": 2.50, "quantity": 5}, "apple": {"price": 1.50, "quantity": 1}, "orange": {"price": 1.00, "quantity": 3}}

# Part 8 of Lab

for item, values in groceryPurchase.items():
    if values["quantity"] == 1:
        print(f"Purchase {values['quantity']} {item} at cost {values['price']} dollar each.")
    else:
        print(f"Purchase {values['quantity']} {item}s at cost {values['price']} dollars each.")
        

  
  
