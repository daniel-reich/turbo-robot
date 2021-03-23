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

def emphasise(txt):
  lst = txt.split()
  return " ".join(word[0].upper()+word[1:].lower() for word in lst)

