"""


In BlackJack, cards are counted with -1, 0, 1 values:

  * 2, 3, 4, 5, 6 are counted as +1
  * 7, 8, 9 are counted as 0
  * 10, J, Q, K, A are counted as -1

Create a function that counts the number and returns it from the list of cards
provided.

### Examples

    count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1
    
    count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6
    
    count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5

### Notes

  * String inputs will always be upper case.
  * You do not need to consider case sensitivity.
  * If the argument is empty, return `0`.
  * No input other than: `2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"`.

"""

def count(deck):
    set1={2, 3, 4, 5, 6 }
    set2={7, 8, 9 }
    set3={10, "J", "Q", "K", "A"}
    d=0
    for i in range(0,len(deck),1):
        if deck[i] in set1:
            d=d+1
        elif deck[i] in set2:
            d=d+0
        else:
            d=d-1
    return d
​
result=count(["A", "A", "K", "Q", "Q", "J"])
print(result)

