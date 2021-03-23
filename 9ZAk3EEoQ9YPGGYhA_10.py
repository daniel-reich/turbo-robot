"""


Create a function that returns any of the items you can afford in the `store`
with the money you have in your `wallet`. Sort the list in alphabetical order.

### Examples

    items_purchase({
      "Water": "$1",
      "Bread": "$3",
      "TV": "$1,000",
      "Fertilizer": "$20"
    }, "$300") ➞ ["Bread", "Fertilizer", "Water"]
    
    items_purchase({
      "Apple": "$4",
      "Honey": "$3",
      "Fan": "$14",
      "Bananas": "$4",
      "Pan": "$100",
      "Spoon": "$2"
      }, "$100") ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]
    
    items_purchase({
      "Phone": "$999",
      "Speakers": "$300",
      "Laptop": "$5,000",
      "PC": "$1200"},
    "$1") ➞ "Nothing"

### Notes

Return `"Nothing"` if you can't afford anything from the `store`.

"""

def items_purchase(store, wallet):
  
  Products = []
  Prices = []
  
  for key, value in store.items():
    Products.append(key)
    Prices.append(value)
  
  Counter = 0
  Length = len(Prices)
  
  while (Counter < Length):
    Item = Prices[Counter]
    Tweak1 = Item.replace("$","")
    Tweak2 = Tweak1.replace(",","")
    Revised = Tweak2
    Prices[Counter] = Revised
    Counter += 1
  
  Available = wallet.replace("$","")
  Available = Available.replace(",","")
  Can_Buy = []
  
  Counter = 0
  Length = len(Prices)
  
  while (Counter < Length):
    Available = int(Available)
    Needed = int(Prices[Counter])
    
    if (Available >= Needed):
      Can_Buy.append(Products[Counter])
      Counter += 1
    else:
      Counter += 1
  
  Answer = sorted(Can_Buy)
  
  if (Answer == []):
    return "Nothing"
  else:
    return Answer

