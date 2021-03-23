"""


Tap code is a way to communicate messages via a series of taps (or knocks) for
each letter in the message. Letters are arranged in a 5x5 _polybius square_ ,
with the letter "K" being moved to the space with "C".

       1  2  3  4  5
    1  A  B C\K D  E
    2  F  G  H  I  J
    3  L  M  N  O  P
    4  Q  R  S  T  U
    5  V  W  X  Y  Z

Each letter is translated by tapping out the _row_ and _column_ number that
the letter appears in, leaving a short pause in-between. If we use "." for
each tap, and a single space to denote the pause:

    text = "break"
    
    "B" = (1, 2) = ". .."
    "R" = (4, 2) = ".... .."
    "E" = (1, 5) = ". ....."
    "A" = (1, 1) = ". ."
    "K" = (1, 3) = ". ..."

Another space is added between the groups of taps for each letter to give the
final code:

    "break" = ". .. .... .. . ..... . . . ..."

Write a function that returns the tap code if given a word, or returns the
translated word (in lower case) if given the tap code.

### Examples

    tap_code("break") ➞ ". .. .... .. . ..... . . . ..."
    
    tap_code(".... ... ... ..... . ..... ... ... .... ....") ➞ "spent"

### Notes

For more information on tap code, please see the resources section. The code
was widely used in WW2 as a way for prisoners to communicate.

"""

alphabet = "abcdefghijlmnopqrstuvwxyz"
def tap_code(text):
  print(text)
  if "." in text:
    result = translate_to_words(text)
  else:
    result = translate_to_code(text)
  return result
​
def translate_to_words(code):
  word = ""
  segments = code.split()
  coded_letters = []
  for i in range(int(len(segments)/2)):
    row_points = segments[i * 2]
    collumn_points = segments[i * 2 + 1]
    coded_letters.append([len(row_points), len(collumn_points)])
  for coded_letter in coded_letters:
    position = (coded_letter[0] - 1) * 5 + coded_letter[1] - 1
    letter = alphabet[position]
    word += letter
  return word
​
def translate_to_code(text):
  code = ""
  words = text.lower().replace("k", "c").split()
  for word in words:
    for letter in word:
      letter_pos = alphabet.find(letter)
      row = letter_pos // 5 + 1
      collumn = letter_pos % 5 + 1
      for i in range(row):
        code += "."
      code += " "
      for i in range(collumn):
        code += "."
      code += " "
  return (code[:-1])

