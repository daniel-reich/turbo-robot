"""


Write a function that accepts a positive integer between `0` and `999`
inclusive and returns a string representation of that integer written in
English.

### Examples

    num_to_eng(0) ➞ "zero"
    
    num_to_eng(18) ➞ "eighteen"
    
    num_to_eng(126) ➞ "one hundred twenty six"
    
    num_to_eng(909) ➞ "nine hundred nine"

### Notes

  * There are no hyphens used (e.g. "thirty five" not "thirty-five").
  * The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

"""

def num_to_eng(n):
  if n == 0:
    return 'zero'
​
  unit = ('','one','two','three','four','five','six','seven','eight','nine')
  tens = ('','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')
  teen = ('ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
  h, t, u = '', '', ''
​
  if n//100:
    h = unit[n//100] + ' hundred'
    n = n%100
​
  if n >= 20:
    t = tens[n//10]
    n = n%10
  elif n >= 10:
    t = teen[n-10]
    n = 0
  
  u = unit[n]
  
  return ' '.join(filter(None,[h,t,u]))

