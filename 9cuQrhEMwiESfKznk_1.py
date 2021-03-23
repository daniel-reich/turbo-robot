"""


This is a companion to my [previous
challenge](https://edabit.com/challenge/mZqMnS3FsL2MPyFMg).

Given an English description of an integer in the range **0 to 999** , devise
a function that returns the integer in numeric form.

### Examples

    eng2nums("four") ➞  4
    
    eng2nums("forty") ➞ 40
    
    eng2nums("six hundred") ➞ 600
    
    eng2nums("one hundred fifteen") ➞ 115
    
    eng2nums("seven hundred sixty seven") ➞ 767

### Notes

  * No hyphens are used in test cases ("twenty three" not "twenty-three").
  * The word "and" is not used: "one hundred three" not "one hundred and three".

"""

def eng2nums(s):
  def find_hundred(s):
    if 'hundred' not in s:
      return False
    else:
      return s.split('hundred')[0].replace(' ', '')
  def find_tenths(s):
    
    words = s.split()
    tens = {'twenty': 'two', 'thirty': 'three', 'forty': 'four', 'fifty': 'five', 'sixty': 'six', 'seventy': 'seven', 'eighty': 'eight', 'ninety': 'nine'}
    
    for word in words:
      if word in tens.keys():
        return tens[word]
    
    return False
  def find_ones(s):
    words = s.split()
​
    digits = 'one,two,three,four,five,six,seven,eight,nine'.split(',')
​
    if words[-1] in digits:
      return words[-1]
    
    return False
  def find_specials(s):
    specials = 'ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen'.split(', ')
​
    for special in specials:
      if special in s:
        return special
    
    return False
  def convert(word):
    words = 'one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
    nums = list(range(1, 20))
​
    words_to_nums = {}
​
    for n in range(19):
      words_to_nums[words[n]] = nums[n]
    
    return words_to_nums[word]
​
  parts = []
  h = find_hundred(s)
​
  if h != False:
    parts.append(convert(h) * 100)
  sp = find_specials(s)
  
  if sp == False:
    t = find_tenths(s)
    if t != False:
      parts.append(convert(t) * 10)
    o = find_ones(s)
    if o != False:
      parts.append(convert(o))
  else:
    parts.append(convert(sp))
  
  return sum(parts)

