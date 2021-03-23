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
  return "".join([txt[i].upper() if i == 0 or txt[i - 1] == " " and isinstance(txt[i], str) else txt[i].lower() if isinstance(txt[i], str) else txt[i] for i in range(0, len(txt))])

