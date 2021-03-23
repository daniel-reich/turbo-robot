"""


Create a function that takes a string as an argument and converts the first
character of each word to uppercase. Return the newly formatted string.

### Examples

    make_title("This is a title") ➞ "This Is A Title"
    
    make_title("capitalize every word") ➞ "Capitalize Every Word"
    
    make_title("I Like Pizza") ➞ "I Like Pizza"
    
    make_title("PIZZA PIZZA PIZZA") ➞ "PIZZA PIZZA PIZZA"

### Notes

  * You can expect a valid string for each test case.
  * Some words may contain more than one uppercase letter (see example #4).

"""

def make_title(txt):
  return ' '.join([x[0].capitalize()+x[1:] for x in txt.split()])

