"""


Create a function which returns `"upper"` if all the letters in a word are
**uppercase** , `"lower"` if **lowercase** and `"mixed"` for any mix of the
two.

### Examples

    get_case("whisper...") ➞ "lower"
    
    get_case("SHOUT!") ➞ "upper"
    
    get_case("Indoor Voice") ➞ "mixed"

### Notes

Ignore punctuation, spaces and numbers.

"""

def get_case(txt):
  return "upper" if txt.isupper() else "lower" if txt.islower() else "mixed"

