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

from itertools import product
​
def crack_pincode(pin):
    d = {'1': '124', '2': '2135', '3': '326', '4': '4157', '5': '52468', 
         '6': '6359', '7': '748', '8': '85790', '9': '968', '0': '08'}
    
    arr = [list(d[n]) for n in pin]
    return sorted([''.join(i) for i in product(*arr)])

