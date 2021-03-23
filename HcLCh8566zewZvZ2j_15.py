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
  if s=="one"   : return 1
  if s=="two"   : return 2
  if s=="three" : return 3 
  if s=="four"  : return 4
  if s=="five"  : return 5
  if s=="six"   : return 6
  if s=="seven" : return 7
  if s=="eight" : return 8 
  if s=="nine"  : return 9
  if s=="zero"  : return 0

