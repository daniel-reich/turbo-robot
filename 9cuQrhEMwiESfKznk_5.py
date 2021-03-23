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
  lookup = {'zero':(1,0),'one': (1 , 1),'two': (1 , 2),'three': (1 , 3),'four': (1 , 4),'five': (1 , 5),'six': (1 , 6),'seven': (1 , 7),'eight': (1 , 8),'nine': (1 , 9),'ten': (1 , 10),'eleven': (1 , 11),'twelve': (1 , 12),'thirteen': (1 , 13),'fourteen': (1 , 14),'fifteen': (1 , 15),'sixteen': (1 , 16),'seventeen': (1 , 17),'eighteen': (1 , 18),'nineteen': (1 , 19),'twenty': (1 , 20),'thirty': (1 , 30),'forty': (1 , 40),'fifty': (1 , 50),'sixty': (1 , 60),'seventy': (1 , 70),'eight': (1 , 80),'ninety': (1 , 90),'hundred': (100 , 100),'thousand': (1000 , 110)
}
  result = 0
​
  for item in s.split(): 
    (weight,val) = lookup[item.lower()]
    if weight == 1:         
      result = result + val
    else:
      result = weight * result      
      
  return result

