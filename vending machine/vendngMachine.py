import random

item_data = [
   {
      "itemId": 0,
      "itemName": "water ",
      'itemPrice': 1.00,
   },{
      "itemId": 1,
      "itemName": "pepsi ",
      'itemPrice': 1.90,
   },{
      "itemId": 2,
      "itemName": "fanta ",
      'itemPrice': 1.50,
   },{
      "itemId": 3,
      "itemName": "coke  ",
      'itemPrice': 2.00,
   },{
      "itemId": 4,
      "itemName": "sprite",
      'itemPrice': 1.20,
   },
]

run = True
price=""
reciept = ""
item = []
for i in range(len(item_data)):
    print(item_data[i])



def vendingMachine(item_data, run, item):
   while run:
      buyItem = int(
         input("\n\nEnter the item code for the item you want to buy: "))
      if buyItem < len(item_data):
         item.append(item_data[buyItem])
      else:
         print("THE PRODUCT ID IS WRONG!")
      #run = False  
      #cost
      cost = (sumItem(item))
      print("your total is: £",cost)
      paymethod = input("Would you like to pay by cash or card? ")
      if paymethod == "cash":
         print("please insert coins")
         total = 0
         run2 = True
         while run2 == True:
            coin = float(input("value of coin entered"))
            total = total + coin
            if total >= cost :
               change = total - cost 
               print("£",change," change due")
               run2 = False
            else:
               cost = cost - total 
               print("£",cost," payment due")

      elif paymethod == "card":
         run3 = True
         while run3 == True:
          cardwork = random.randint(1,9)
          if cardwork >= 5:
            print("payment successful")
            print("please collect your ",item)
            run3 = False
            run = False
          else:
            print("payment unsuccessful please try again")
   
#error outputting item name after payment completed 
#test cash payment method


#
def sumItem(item):
   sumItems = 0
   for i in item:
      sumItems += i["itemPrice"]
   return sumItems
  
def createReceipt(item, reciept):
   for i in item:
      reciept += f"""
      \t{i["itemName"]}
"""
#main code 
vendingMachine(item_data, run, item)