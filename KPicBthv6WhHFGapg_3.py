"""


Create a function that returns the **number of syllables** in a simple string.
The string is made up of _short repeated words_ like `"Lalalalalalala"` (which
would have _7 syllables_ ).

### Examples

    count_syllables("Hehehehehehe") ➞ 6
    
    count_syllables("bobobobobobobobo") ➞ 8
    
    count_syllables("NANANA") ➞ 3

### Notes

  * For simplicity, please note that each syllable will consist of two letters only.
  * Your code should accept strings of any case (upper, lower and mixed case).

"""

def count_syllables(txt):
  if not isinstance(txt, str):
    raise TypeError('txt need to be a str')
  return sum([txt.count(letter) for letter in 'aeyuioAEYUIO'])

