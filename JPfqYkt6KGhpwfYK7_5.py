"""


Create a function that **replaces "the"** in the sentence with **"an"** or
**"a"**. Remember that if the _next word_ begins with a _vowel_ , use
**"an"**. In the case of a _consonant_ , use **"a"**.

### Examples

    replace_the("the dog and the envelope") ➞ "a dog and an envelope"
    
    replace_the("the boy ran at the wall") ➞ "a boy ran at a wall"
    
    replace_the("the egg, the spoon and the espionage") ➞ "an egg, a spoon and an espionage"

### Notes

  * Sentences will always be in **lowercase**.
  * The last word of the sentence will never be "the".
  * This won't cover edge cases such as _"an hour"_ or _"a unique thing"_ (since they _sound_ differently to the rule).

"""

import re
def replace_the(txt):
    words = txt.split()
    i = 0
    lst = []
    for ch in words:
        if ch == 'the' and re.match(r"^[aeiou]", words[i+1]):
            lst.append(ch.replace('the', 'an'))
            i += 1
        elif ch == 'the' and re.match(r"^[^aeiou]", words[i+1]):
            lst.append(ch.replace('the', 'a'))
            i += 1
        else:
            lst.append(ch)
            i += 1
    return " ".join(lst)

