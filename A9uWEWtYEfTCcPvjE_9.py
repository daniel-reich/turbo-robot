"""


Create a function that returns a list of the most important items purchasable
with a given budget. You will be given a dictionary `dct` containing items and
their respective price and importance, and you will also be given a budget `b`
to restrict the number of items you can buy. The importance can only be from
1-10, whereas the price and budget can be anything.

### Example

    price_importance_sort({
      "apples": { "price": 5, "importance": 3 },
      "oranges": { "price": 3, "importance": 2},
      "pears": { "price": 2,  "importance": 2}
    }, 5) ➞ ["oranges", "pears"]

The oranges and pears can be purchased at budget with a total importance of
`4`. Apples and oranges or pears are not able to be purchased due to the
budget and apples themselves only have an importance value of `3`, making the
oranges/pears group preferable.

### Notes

  * More importance is better, not worse (it isn't a 1st/2nd/3rd ranking).
  * The whole budget may be used.
  * In the case of a tie, use the cheaper/more important of the two.
  * Order the final list alphabetically.

"""

def price_importance_sort(dct,b):
    total,newdct,totalprice=[],{},0
    def valof(item,ia):
        return dct[list(dct.keys())[list(dct.keys()).index(item)]][ia]
    for i in list(dct.keys()):
        price,imps=valof(i,'price'),valof(i,'importance')
        newdct.update({price/imps: i})
    newdctnums=sorted(newdct)
    for i in newdctnums:
        if valof(newdct[i],'price')+totalprice<=b:
            total.append(newdct[i])
            totalprice+=valof(newdct[i],'price')
        else:
            return sorted(total)

