"""


Create a function that outputs the result of a math expression in words.

### Examples

    worded_math("One plus one") ➞ "Two"
    
    worded_math("zero Plus one") ➞ "One"
    
    worded_math("one minus one") ➞ "Zero"

### Notes

  * Expect only the operations `plus` and `minus`.
  * Expect to only get numbers and answers from `0` to `2`.
  * The first letter of the answer must be capitalised.

"""

def worded_math(equ):
    dic = {"zero":0, "one":1, "two":2, 0:"Zero", 1:"One", 2:"Two"}
    lst = equ.split(" ")
    if lst[1].lower() == "plus":
        return dic[dic[lst[0].lower()]+dic[lst[2].lower()]]
    else:
        return dic[dic[lst[0].lower()]-dic[lst[2].lower()]]

