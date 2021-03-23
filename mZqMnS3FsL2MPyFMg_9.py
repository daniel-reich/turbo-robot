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
  one_to_nineteen = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'forteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
  twenty_to_ninety = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
  ans = []
  if n >= 100:
    ans += [one_to_nineteen[n//100]] + ['hundred']
  if n%100 >= 20:
    ans.append(twenty_to_ninety[(n%100)//10])
    if n%10 > 0:
      ans.append(one_to_nineteen[n%10])
  elif n%100 in one_to_nineteen:
    ans.append(one_to_nineteen[n%100])
  return ' '.join(ans)

