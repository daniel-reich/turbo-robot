"""


Check the principles of minimalist code in the [intro to the first
challenge](https://edabit.com/challenge/2XLjgZhmACph76Pkr).

In the **Code** tab you will find a code that is missing a single character in
order to pass the tests. However, your goal is to submit a function as
**minimalist** as possible. Use the tips in the tips section below.

Write a function that returns the strings:

  * `"both"` if both given booleans `a` and `b` are `True`.
  * `"first"` if only `a` is `True`.
  * `"second"` if only `b` is `True` .
  * `"neither"` if both `a` and `b` are `False`.

### Tips

If-else statements can be written as a oneliner using Python's **ternary
operator**.

For example, the code:

    def startswith(name):
      if name[0] in "AEIOU":
        return "vowel"
      else:
        return "consonant"

Can be simplified to:

    def startswith(name):
      return "vowel" if name[0] in "AEIOU" else "consonant"

### Bonus

You can concatenate as many ternary operators as you want. However,
concatenating too many will definitely diminish the readability of your code.

    "majority" if  x > 50 else "minority" if x < 50 else "draw"

### Notes

  * This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your **suggestions** in the **Comments**.
  *  _ **Readability**_ is indeed a subjective concept. **Let's discuss it!** Feel free to leave your opinion in the **Comments**.
  * You can find all the exercises in this series [over here]().

"""

def are_true(a, b):
  if a  == True:
    if b == True:
      return "both"
    else:
      return "first"
  elif b == True:
    return "second"
  else:
    return "neither"

