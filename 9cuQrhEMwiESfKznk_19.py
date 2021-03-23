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
  ones={ 'one':   1, 'eleven':     11,
       'two':   2, 'twelve':     12,
       'three': 3, 'thirteen':   13,
       'four':  4, 'fourteen':   14,
       'five':  5, 'fifteen':    15,
       'six':   6, 'sixteen':    16,
       'seven': 7, 'seventeen':  17,
       'eight': 8, 'eighteen':   18,
       'nine':  9, 'nineteen':   19,
       'zero':  0}
  tens={ 'ten':     10,
       'twenty':  20,
       'thirty':  30,
       'forty':   40,
       'fifty':   50,
       'sixty':   60,
       'seventy': 70,
       'eighty':  80,
       'ninety':  90 }
  A=s.split()
  res=''
  for x in A:
    if x in ones:
      res+='+'+str(ones[x])
    elif x in tens:
      res+='+'+str(tens[x])
    else:
      res+='*100'
  if res[0]=='+':
    res=res[1:]
  return eval(res)

