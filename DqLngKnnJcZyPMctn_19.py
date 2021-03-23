"""


Create a function that takes a list of integers that represent the amount in
dollars that a single stock is worth, and return the maximum profit that could
have been made by buying stock on day **x** and selling stock on day **y**
where **y >x**.

If given the following list:

    [44, 30, 24, 32, 35, 30, 40, 38, 15]

... your program should return `16` because at index 2 the stock was worth $24
and at the index 6 the stock was then worth $40, so if you bought the stock at
24 and sold it on 40, you would have made a profit of $16, which is the
maximum profit that could have been made with this list of stock prices.

If there is no profit that could have been made with the stock prices, then
your program should return `-1` (e.g. `[[10, 9, 8, 2]]` should return `-1`).

### Examples

    stock_picker([10, 12, 4, 5, 9]) ➞ 5
    
    stock_picker([14, 20, 4, 12, 5, 11]) ➞ 8
    
    stock_picker([80, 60, 10, 8]) ➞ -1

### Notes

N/A

"""

def stock_picker(lst):
  if sorted(lst,reverse=True)==lst:
    return -1
  lmax,lmin=max(lst),min(lst)
  limax,limin=map(lst.index,[lmax,lmin])
  if limax>limin:
    return lmax-lmin
  lmin1,lmax1=min(lst[:limax+1]),max(lst[limin:])
  return max(max([lmax-lmin1,lmax1-lmin]),stock_picker(lst[limax+1:limin]))

