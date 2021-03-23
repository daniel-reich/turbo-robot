"""


It is important to be happy! Therefore, you must create a function that takes
a sentence containing sad faces and turn them into happy ones! This involves
changing only the mouths.

  *  **Sad face examples:** `:(` `8(` `x(` `;(`
  *  **Happy face examples:** `:)` `8)` `x)` `;)`

Make sure to only change the face if there are eyes before them, _round(3.4)_
wouldn't become _round)3.4)_ (for example).

### Examples

    make_happy("My current mood: :(") ➞ "My current mood: :)"
    
    make_happy("I was hungry 8(") ➞ "I was hungry 8)"
    
    make_happy("print('x(')") ➞ "print('x)')"

### Notes

Faces such as `:(((((((` are not included.

"""

import re
def make_happy(txt):
  regex = r'(?<=[:8x;])\('
  return re.sub(regex, ")" ,txt)

