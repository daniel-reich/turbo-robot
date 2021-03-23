"""


The normal `title()` function in Python _capitalises the first letter of every
word_ in a given sentence, leaving all the other letters as _lowercase_.

The goal of this challenge is to create a `reverse_title()` function, which
achieves the complete opposite! Make the first letter of every word
**lowercase** , and the rest **uppercase!**

###  Examples

    reverse_title("this is a title") ➞ "tHIS iS a tITLE"
    
    reverse_title("BOLD AND BRASH!") ➞ "bOLD aND bRASH!"
    
    reverse_title("Elephants dance about bravely in Thailand") ➞ "eLEPHANTS dANCE aBOUT bRAVELY iN tHAILAND"

### Notes

N/A

"""

def reverse_title(txt):
  txt1 = txt.title()
  return txt1.swapcase()

