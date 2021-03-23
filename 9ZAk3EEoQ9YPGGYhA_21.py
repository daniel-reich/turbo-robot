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
    l = list(store.items())
    lprice = list(map(lambda x:int(x[1].replace(',','')[1:]),l))
    ans = []
    for i in range(len(lprice)):
        if int(wallet[1:])>=lprice[i]:ans.append(l[i][0])
    return  sorted(ans) if len(ans)!=0 else 'Nothing'

