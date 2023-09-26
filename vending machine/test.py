items_data = [
   {
      "itemId": 0,
      "itemName": "Dairy Milk",
      'itemPrice': 120,
   },{
      "itemId": 1,
      "itemName": "5Star",
      'itemPrice': 30,
   },{
      "itemId": 2,
      "itemName": "perk",
      'itemPrice': 50,
   },{
      "itemId": 3,
      "itemName": "Burger",
      'itemPrice': 200,
   },{
      "itemId": 4,
      "itemName": "Pizza",
      'itemPrice': 300,
   },
]
item = []
reciept = """
\t\tPRODUCT NAME -- COST
"""
sum = 0
run = True

print("------- Vending Machine Program with Python-------\n\n")
print("----------The Items In Stock Are----------\n\n")


for i in items_data:
   print(
      f"Item: {i['itemName']} --- Price: {i['itemPrice']} --- Item ID: {i['itemId']}")


def vendingMachine(items_data, run, item):
   while run:
      buyItem = int(
         input("\n\nEnter the item code for the item you want to buy: "))
      if buyItem < len(items_data):
         item.append(items_data[buyItem])
      else:
         print("THE PRODUCT ID IS WRONG!")




vendingMachine(items_data, run, item)