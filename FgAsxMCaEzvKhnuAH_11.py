"""


Create a function that takes an array of strings of arbitrary dimensionality
(`[]`, `[][]`, `[][][]`, etc) and returns the deep_sum of every separate
number in each string in the array.

### Examples

    deep_sum(["1",  "five",  "2wenty",  "thr33"]) ➞ 36
    
    deep_sum([["1X2",  "t3n"], ["1024", "5", "64"]]) ➞ 1099
    
    deep_sum([[["1"], "10v3"],  ["738h"],  [["s0"],  ["1mu4ch3"], "-1s0"]]) ➞ 759

### Notes

  * Numbers in strings can be negative, but will all be base-10 integers.
  * Negative numbers may directly follow another number.
  * The hyphen or minus character ("-") does not only occur in numbers.
  * Arrays may be ragged or empty.

"""

def deep_sum(lst):
  def get_ints(string):
    digits = '0123456789'
    nums = []
    num = ''
    negative = False
    
    for l8r in string:
      if l8r in digits:
        num += l8r
      elif l8r == '-' and negative == False:
        if num != '':
          nums.append(int(num))
          num = ''
        num += l8r
        negative = True
      elif l8r == '-' and negative == True:
        if num != '-':
          nums.append(int(num))
        num = l8r
      else:
        if negative == True:
          if num != '-':
            nums.append(int(num))
          num = ''
          negative = False
        elif num != '':
          nums.append(int(num))
          num = ''
        else:
          continue
    
    if num != '':
      nums.append(int(num))
      num = ''
#   print(nums)
    return nums
  def denester(lst):
    l = str(lst).replace('[', '').replace(']','').split(', ')
    return [i for i in l if len(i) > 0 and i != '']
  
  #print(denester(lst))
  tr = [sum(get_ints(string)) for string in denester(lst)]
# print(tr)
  return sum(tr)

