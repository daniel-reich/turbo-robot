"""


 **Mubashir** was playing with dominos. He concluded that:

  * If the first domino is pushed over, it will **keep tipping next dominos to its right**.
  * Reaction will stop if a domino is **already tipped over** , or if there is an **empty space**.

![Mubashir](https://edabit-challenges.s3.amazonaws.com/329666480_orig.gif)

Create a function which takes a string of current status of the `dominos` and
returns the string after **dominos chain reaction**.

  * "|" represents a standing domino.
  * "/" represents a tripped domino.
  * " " represents an empty space.

### Examples

    domino_chain("||| ||||//| |/") ➞ "/// ||||//| |/"
    // A space will stop the reaction.
    
    domino_chain("||//||") ➞ "////||"
    // An already tripped domino will stop the reaction.
    
    domino_chain("||||") ➞ "////"

### Notes

N/A

"""

from re import sub
def domino_chain(dominos):
    return sub(r"^[|]+", lambda m: r"/" * len(m.group()), dominos)

