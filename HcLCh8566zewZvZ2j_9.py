"""


Create a function that returns a number, based on the string provided. Here is
a list of all digits (if you are non english speaker):

String| Number  
---|---  
"one"| 1  
"two"| 2  
"three"| 3  
"four"| 4  
"five"| 5  
"six"| 6  
"seven"| 7  
"eight"| 8  
"nine"| 9  
"zero"| 0  
  
### Examples

    word("one") ➞ 1
    
    word("two") ➞ 2
    
    word("nine") ➞ 9

### Notes

All numbers will be single digit positive integers.

"""

def word(s):
  d = {
  'one' : 1,
  'two' : 2,
  'three' : 3,
  'four' : 4,
  'five' : 5,
  'six' : 6,
  'seven' : 7,
  'eight' : 8,
  'nine' : 9,
  'zero' : 0
  }
  return d[s]

