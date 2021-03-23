"""


Character recognition software often makes mistakes when documents (especially
old ones written with a typewriter) are digitized.

Your task is to correct the errors in the digitized text. You only have to
handle the following mistakes:

  * A is misinterpreted as 4
  * S is misinterpreted as 5
  * O is misinterpreted as 0
  * I is misinterpreted as 1

The test cases contain numbers only by mistake.

### Examples

    keyboard_mistakes("MUB45H1R") ➞ "MUBASHIR"
    
    keyboard_mistakes("DUBL1N") ➞ "DUBLIN"
    
    keyboard_mistakes("51NG4P0RE") ➞ "SINGAPORE"

### Notes

N/A

"""

def keyboard_mistakes(txt):
  a_word = list(txt)
  word = ''
  for position, letter in enumerate(a_word):
    if letter == '4':
      word += 'A'
    elif letter == '5':
      word += 'S'
    elif letter == '1':
      word += 'I'
    elif letter == '0':
      word += 'O'
    else:
      word += a_word[position]
  return word

