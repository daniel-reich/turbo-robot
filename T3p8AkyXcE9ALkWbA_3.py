"""


Given a sandwich (as a _list_ ), return a list of fillings inside the
sandwich. This involves **ignoring** the first and last elements.

### Examples

    get_fillings(["bread", "ham", "cheese", "ham", "bread"]) ➞ ["ham", "cheese", "ham"]
    
    get_fillings(["bread", "sausage", "tomato", "bread"]) ➞ ["sausage", "tomato"]
    
    get_fillings(["bread", "lettuce", "bacon", "tomato", "bread"]) ➞ ["lettuce", "bacon", "tomato"]

### Notes

The first and last elements will always be `"bread"`.

"""

def get_fillings(sandwich):
  return sandwich[1:-1]

