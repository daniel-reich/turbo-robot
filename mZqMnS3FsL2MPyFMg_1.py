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
  key = [['zero', 'ten '], 
       ['one', 'eleven '], 
       ['two', 'twen'], 
       ['three', 'thir'], 
       ['four', 'four'], 
       ['five', 'fif'], 
       ['six', 'six'], 
       ['seven', 'seven'], 
       ['eight', 'eigh'], 
       ['nine', 'nine']]
​
  res = []
  hun = n//100 % 10
  ten = n//10 % 10
  uni = n % 10
​
  if hun: 
    res.append(key[hun][0] + ' hundred') 
  if ten > 1: 
    res.append(key[ten][1] + 'ty')
  if ten == 1: 
    res.append((key[uni][1] + 'teen').replace(' teen', '').replace('twenteen', 'twelve'))
  elif uni:
    res.append(key[uni][0])
  
  return key[uni][0] if not res else ' '.join(res)

