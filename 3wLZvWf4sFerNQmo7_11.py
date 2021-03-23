"""


Given two strings comprised of `+` and `-`, return a new string which shows
how the two strings interact in the following way:

  * When positives and positives interact, they _remain positive_.
  * When negatives and negatives interact, they _remain negative_.
  * But when negatives and positives interact, they _become neutral_ , and are shown as the number `0`.

### Worked Example

    neutralise("+-+", "+--") ➞ "+-0"
    # Compare the first characters of each string, then the next in turn.
    # "+" against a "+" returns another "+".
    # "-" against a "-" returns another "-".
    # "+" against a "-" returns "0".
    # Return the string of characters.

### Examples

    neutralise("--++--", "++--++") ➞ "000000"
    
    neutralise("-+-+-+", "-+-+-+") ➞ "-+-+-+"
    
    neutralise("-++-", "-+-+") ➞ "-+00"

### Notes

The two strings will be the same length.

"""

def neutralise(lst1, lst2):
  a1 = list(lst1)
  b2 = list(lst2)
  c = []
  for i in range(len(a1)):
    c.append(a1[i]+b2[i])
​
  result=[]
​
  for i in c:
    if i == '++':
      result.append('+')
    elif i == '--':
      result.append('-')
    elif i == '+-' or i == '-+':
      result.append('0')
​
  return ''.join(result)

