"""


Given a number _between 1-26_ , return what letter is at _that position_ in
the alphabet. Return `"invalid"` if the number given is not within that range,
or isn't an integer.

### Examples

    letter_at_position(1) ➞ "a"
    
    letter_at_position(26.0) ➞ "z"
    
    letter_at_position(0) ➞ "invalid"
    
    letter_at_position(4.5) ➞ "invalid"

### Notes

  * Return a lowercase letter.
  * Numbers that end with `".0"` are valid.

"""

letter_at_position = lambda x: 'invalid' if x % 1 \
  or x not in range(1, 27) else chr(int(x) + 96)

