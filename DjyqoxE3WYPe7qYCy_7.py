"""


Given a string, reverse all the words which have odd length. The even length
words are not changed.

### Examples

    reverse_odd("Bananas") ➞ "sananaB"
    
    reverse_odd("One two three four") ➞ "enO owt eerht four"
    
    reverse_odd("Make sure uoy only esrever sdrow of ddo length")
    ➞ "Make sure you only reverse words of odd length"

### Notes

There is exactly one space between each word and no punctuation is used.

"""

def reverse_odd(string):
  words = string.split(" ");
  return " ".join(word[::-1] if len(word) %2 != 0 else word for word in words);

