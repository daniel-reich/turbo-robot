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

def replace_the(txt):
  l = []
  txt = txt.split()
  for i in range(len(txt)):
    if txt[i] == "the" and txt[i + 1][0] in "aeiou":
      l.append("an")
    elif txt[i] == "the" and txt[i + 1][0] not in "aeiou":
      l.append("a")
    else:
      l.append(txt[i])
​
  return " ".join(l)

