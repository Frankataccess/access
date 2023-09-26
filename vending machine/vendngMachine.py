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
      if buyItem == 0:
         item_name = "water"
      elif buyItem == 1:
         item_name = "pepsi"
      elif buyItem == 2:
         item_name = "fanta"
      elif buyItem == 3:
         item_name = "coke"
      elif buyItem == 4:   
         item_name = "sprite"
      #cost
      cost = (sumItem(item))
      print("your total is: £",cost)
      paymethod = input("Would you like to pay by cash or card? ")
      if paymethod == "cash":
         print("please insert coins")
         total = 0
         run2 = True
         while run2 == True:
            coin = float(input("value of coin entered: £"))
            total = total + coin
            total = round(total,2)
            if total >= cost :
               change = total - cost 
               change = round(change,2)
               print("£{:0.2f}.".format(change), "change due")
               print ("please collect your",item_name)
               run2 = False
            else:
               cost = cost - total 
               cost = round(cost,2)
               total = cost
               print("£{:0.2f}.".format(cost)," payment due")
      elif paymethod == "card":
         run3 = True
         retry = "y"
         while run3 == True:
          cardwork = random.randint(1,9)
          if cardwork >= 5:
            print("payment successful")
            print("please collect your ",item_name)
            run3 = False
            run = False
          elif cardwork < 5:
            retry = input("payment unsuccessful please try again y/n: ")
            if retry == "n":
               print("payment aborted")
               run3 = False
            else:
               run3 = True
       
   
#cash logic error returning change

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