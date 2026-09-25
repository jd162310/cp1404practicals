  # get number of items and each items price
  # Calculate the total price of the items
  # if total price is over $100 then 10% discount is applied
number_of_items = int(input(("Weclome to the shopping calculator, please enter the number of items: ")))
total_price = 0  # starter price for the total
while number_of_items < 0:
    print("not a valid number of items, cannot have zero or negative items")
    number_of_items = int(input("enter a valid number of items please "))
if number_of_items == 0:
    print(f"your total cost for this shopping trip is: ${total_price}")
else:
    for i in range(1, number_of_items + 1):
        item_price = float(input(f"what is the price of item {i}? "))
        total_price = float(total_price) + item_price
if total_price > 100:
    total_price = total_price - (total_price * 0.1)
    print(f"Your total cost for this shopping trip is: ${total_price:.2f}")
elif 0 < total_price <= 100:
    print(f"your total cost for this shopping trip is: ${total_price:.2f}")
else:
    print()