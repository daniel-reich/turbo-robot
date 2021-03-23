"""


Create a function that will remove any repeated charcter(s) in a word passed
to the function. Not just consecutive characters, but characters repeating
anywhere in the input.

### Examples

    unrepeated("hello") ➞ "helo"
    
    unrepeated("aaaaa") ➞ "a"
    
    unrepeated("WWE!!!") ➞ "WE!"
    
    unrepeated("call 911") ➞ "cal 91"

### Notes

  * No more than two words will be passed in the tests.
  * Input includes special characters and numbers.

"""

def unrepeated(txt):
  letters = []
  for i in txt:
    if i not in letters:
      letters.append(i)
  return ''.join(letters)

