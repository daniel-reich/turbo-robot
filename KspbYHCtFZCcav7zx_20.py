"""
The facts are:

  1. You've just finished dinner.
  2. You love spicy food but your friend hates it.

Given your friend's unfortunate taste preferences, you decide to **split the
bill only for non-spicy items**. You will pay in full for the spicy dishes.

Given two ordered lists, one classifying the dishes as spicy vs. non-spicy and
the other listing their prices, write a function that outputs a list where the
first element is **how much you pay** and the second element is **how much
your friend pays**.

    bill_split(["S", "N", "S", "S"], [13, 18, 15, 4]) ➞ [41, 9]
    
    # Since:
    # You pay: [13, 9, 15, 4] = 41
    # Friend pays: [0, 9, 0, 0] = 9

### Examples

    bill_split(["N", "S", "N"], [10, 10, 20]) ➞ [25, 15]
    # You pay for half of both "N" dishes (5 + 10) and entirely pay for the "S" dish (10).
    
    bill_split(["N", "N"], [10, 10]) ➞ [10, 10]
    
    bill_split(["S", "N"], [41, 10]) ➞ [46, 5]

### Notes

  * The dishes are in the same order for both input lists.
  * Remember to output a list in this order: `[your payment, friend's payment]`
  * The list will contain at least one non-spicy dish `N` (you're not going to let your poor friend go hungry, are you?).
  * Express both payments as integers.

"""

def bill_split(spicy, cost):
  you = 0
  fren = 0
  for i in range(len(spicy)):
    if spicy[i] == 'S':
      you += cost[i]
    else:
      you += cost[i]/2
      fren += cost[i]/2
  return [you,fren]

