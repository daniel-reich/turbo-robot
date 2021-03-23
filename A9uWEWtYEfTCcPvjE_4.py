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

from collections import defaultdict
def price_importance_sort(dct, b):
    prices = defaultdict(list)
    for i,x in dct.items():
        prices[x['price']].append(i)
    p = sorted(list(prices.keys()))
    a  = [p[0]] + p
    for x in prices:
        prices[x] = sorted(prices[x], key=lambda x: dct[x]['importance'])
    start = -1
    for x in range(len(p)-1, -1, -1):
        if p[x] <= b:
            start = x-1
            break
    out = []
    for x in range(max(start, 0)+1):
        for _ in range(2):
            if p[x] <= b and prices[p[x]]:
                out.append(prices[p[x]].pop())
                b -= p[x]
    return sorted(out)

