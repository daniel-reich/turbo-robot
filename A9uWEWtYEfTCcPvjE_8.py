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

from itertools import combinations
def price_importance_sort(d, b):
    lst = []
    for k, val in d.items():
        sub_lst = [val['price'], val['importance'], k]
        lst.append(sub_lst)
    lst_fit = []
    for n in range(len(lst), 0, -1):
        for comb in combinations(lst, n):
            total_p = 0
            total_i = 0
            for item in comb:
                total_p += item[0]
                total_i += item[1]
            if total_p <= b:
                lst_fit.append((total_i, total_p, list(comb)))
    lst_fit.sort(key=lambda x: (-x[0], x[1]))
    if lst_fit[0][0] == lst_fit[1][0]:
        print('tie')
    res = [sub_lst[2] for sub_lst in lst_fit[0][2]]
    return sorted(res)

