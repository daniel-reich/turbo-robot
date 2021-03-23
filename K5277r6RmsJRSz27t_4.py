"""


The challenge is to recreate the functionality of the `title()` method into a
function called `emphasise()`. The `title()` method capitalises the first
letter of _every word_ and lowercases all of the other letters in the word.

### Examples

    emphasise("hello world") ➞ "Hello World"
    
    emphasise("GOOD MORNING") ➞ "Good Morning"
    
    emphasise("99 red balloons!") ➞ "99 Red Balloons!"

### Notes

  * You won't run into any issues when dealing with numbers in strings.
  * Please don't use the `title()` method directly :(

"""

def emphasise(string):
  s = ''
  for i in range(len(string)):
    if i == 0:
      s += string[i].upper()
    elif string[i - 1] != " ":
      s += string[i].lower() 
    else:
      s += string[i].upper()
  return s

