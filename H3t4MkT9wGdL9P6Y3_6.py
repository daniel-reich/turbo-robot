"""


Create a function that determines whether a number is **Oddish** or
**Evenish**. A number is **Oddish** if the sum of all of its digits is odd,
and a number is **Evenish** if the sum of all of its digits is even. If a
number is **Oddish** , return `"Oddish"`. Otherwise, return `"Evenish"`.

For example, `oddish_or_evenish(121)` should return `"Evenish"`, since 1 + 2 +
1 = 4. `oddish_or_evenish(41)` should return `"Oddish"`, since 4 + 1 = 5.

### Examples

    oddish_or_evenish(43) ➞ "Oddish"
    # 4 + 3 = 7
    # 7 % 2 = 1
    
    oddish_or_evenish(373) ➞ "Oddish"
    # 3 + 7 + 3 = 13
    # 13 % 2 = 1
    
    oddish_or_evenish(4433) ➞ "Evenish"
    # 4 + 4 + 3 + 3 = 14
    # 14 % 2 = 0

### Notes

N/A

"""

def oddish_or_evenish(num):
  num = str(num)
  sum1 = 0
  for i in num:
    sum1 +=  int(i)
  if sum1 %2 == 0:
    return "Evenish"
  else:
    return "Oddish"

