items = [
   {
      "itemId": 0,
      "itemName": "water",
      'itemPrice': 1.00,
   },{
      "itemId": 1,
      "itemName": "pepsi",
      'itemPrice': 1.90,
   },{
      "itemId": 2,
      "itemName": "fanta",
      'itemPrice': 1.50,
   },{
      "itemId": 3,
      "itemName": "coke",
      'itemPrice': 2.00,
   },{
      "itemId": 4,
      "itemName": "sprite",
      'itemPrice': 1.20,
   },
]

run = True
choice = 0
for i in range(len(items)):
    print(items[i])

def vendingmachine(items,run,choice):
    while run:
        buy_item = int(input("enter the number of the item you want to select"))
    if buy_item < len(items):
         choice.append(items[buy_item])
    else:
        print("please eneter a valid item code")