"""


Check the principles of minimalist code in the [intro to the first
challenge](https://edabit.com/challenge/2XLjgZhmACph76Pkr).

In the **Code** tab you will find a code that is missing a single character in
order to pass the tests. However, your goal is to submit a function as
**minimalist** as possible. Use the tips in the tips section below.

Write a function that returns the boolean `True` if the given two lists **do
not share** any numbers, and `False` otherwise.

### Tips

The operators `in` and `not in` test for **membership**. `x in s` evaluates to
`True` if `x` is a member of `s`, and `False` otherwise.

For example, the code:

    def startswithvowel(word):
        for vowel in "aeiou":
            if word[0] == vowel:
                return True
        return False

Can be simplified to:

    def startswithvowel(word):
        return word[0] in "aeiou"

### Bonus

Here's some more examples.

    12 in [1, 50, 12, 43, 7] ➞ True
    1 in [12, 111111, "x"] ➞ False
    [3, 4] in [1, 2, 3, 4, 5] ➞ False
    3 in (True, 3, ["odd", "even"]) ➞ True
    "odd" in (True, 3, ["odd", "even"]) ➞ False
    "hello" in "hellomyfriend" ➞ True
    
    "myfriend" not in "hello my friend" ➞ True
    "bye" not in "bye my friend" ➞ False
    2 not in {0: "even", 1: "odd"} ➞ True
    1 not in {0: "even", 1: "odd"} ➞ False

### Notes

  * This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your **suggestions** in the **Comments**.
  *  _ **Readability**_ is indeed a subjective concept. **Let's discuss it!** Feel free to leave your opinion in the **Comments**.
  * You can find all the exercises in this series [over here]().

"""

def not_share(lst1, lst2):
  return set(lst1).isdisjoint(lst2)

