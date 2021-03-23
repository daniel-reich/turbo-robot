"""


Create a function that transforms sentences ending with multiple question
marks `?` or exclamation marks `!` into a sentence only ending with one
without changing punctuation in the middle of the sentences.

### Examples

    no_yelling("What went wrong?????????") ➞ "What went wrong?"
    
    no_yelling("Oh my goodness!!!") ➞ "Oh my goodness!"
    
    no_yelling("I just!!! can!!! not!!! believe!!! it!!!") ➞ "I just!!! can!!! not!!! believe!!! it!"
    # Only change repeating punctuation at the end of the sentence.
    
    no_yelling("Oh my goodness!") ➞ "Oh my goodness!"
    # Do not change sentences where there exists only one or zero exclamation marks/question marks.
    
    no_yelling("I just cannot believe it.") ➞ "I just cannot believe it."

### Notes

  * Only change **ending punctuation** \- keep the exclamation marks or question marks in the middle of the sentence the same (see third example).
  * Don't worry about mixed punctuation (no cases that end in something like `?!??!`).
  * Keep sentences that do not have question/exclamation marks the same.

"""

import re
​
def no_yelling(phrase):
    x = ""
    yellRegex = re.compile(r"\!+$|\?+$")
    punc = "".join(yellRegex.findall(phrase.split()[-1]))
    if "?" in punc:
        x += "?"
    elif "!" in punc:
        x += "!"
    if len(phrase.split()) == 1:
        return phrase.replace(punc, x)
    else:
        return " ".join(phrase.split()[:-1]) + " " + phrase.split()[-1].replace(punc, x)

