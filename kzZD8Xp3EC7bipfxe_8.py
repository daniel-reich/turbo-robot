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
  equ=equ.lower()
  lst=equ.split(" ")
  temp=0
  for i in range(len(lst)):
    if lst[i]=="one":
      lst[i]=1
    elif lst[i]=="zero":
      lst[i]=0
  if lst[1]=="plus":
    temp=lst[0]+lst[2]
  elif lst[1]=="minus":
    temp=lst[0]-lst[2]
  if temp==0:
    return "Zero"
  elif temp==1:
    return "One"
  elif temp==2:
    return "Two"

