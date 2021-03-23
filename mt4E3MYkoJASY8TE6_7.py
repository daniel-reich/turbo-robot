"""


Given a keypad that has the following layout:

    ┌───┬───┬───┐
    │ 1 │ 2 │ 3 │
    ├───┼───┼───┤
    │ 4 │ 5 │ 6 │
    ├───┼───┼───┤
    │ 7 │ 8 │ 9 │
    └───┼───┼───┘
        │ 0 │
        └───┘

Your secret agent **Mubashir** has already given you a pincode. However, he
also said it's possible that each of the digits he saw could be another
adjacent digit (horizontally or vertically, but not diagonally).

Suppose the secret agent has given you the code: **46** :

    # Instead of the 4 it could also be 1, 5, or 7.
    # Instead of the 6 it could also be 3, 5, or 9.
    
    crack_pincode("46") ➞
    ["13","15","16","19","43","45","46","49","53","55","56","59","73","75","76","79"]

Create a function that takes an argument of `pincode` informed by your secret
agent and returns a list of **all possible variations** of the pin codes.

### Examples

    crack_pincode("0") ➞ ["0", "8"]
    
    crack_pincode("2") ➞ ["1", "2", "3", "5"]
    
    crack_pincode("007") ➞ ["004","007","008","084","087","088","804","807","808","884","887","888"]

### Notes

All pin codes must be strings, because of potentially leading `0`s.

"""

class Keypad:
  class Key:
​
    def __init__(self, val, near):
      self.v = val
      self.n = near + [val]
  
  one = Key(1, [2,4])
  two = Key(2,[1,3,5])
  three = Key(3,[2,6])
  four = Key(4, [1,7,5])
  five = Key(5,[2,4,6,8])
  six = Key(6,[5,3,9])
  seven = Key(7,[4,8])
  eight = Key(8,[7,5,9,0])
  nine = Key(9,[8,6])
  zero = Key(0,[8])
​
  dic = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}
​
  def possabilities(keys):
    from itertools import product as pro 
​
    lst_of_pobs = [Keypad.dic[int(key)].n for key in keys]
​
    products =  lst_of_pobs[0]
​
    for i in range(1, len(lst_of_pobs)):
      products = pro(products, lst_of_pobs[i])
​
    tr = []
​
    for p in products:
      try:
        tr.append(''.join(str(digit).replace('(','').replace(', ', '').replace(')','') for digit in p))
      except TypeError:
        tr = [str(i) for i in products]
    
    return list(sorted(tr))
​
​
def crack_pincode(pincode):
​
  return Keypad.possabilities(pincode)

