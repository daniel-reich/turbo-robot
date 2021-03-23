"""


Check the principles of minimalist code in the [intro to the first
challenge](https://edabit.com/challenge/2XLjgZhmACph76Pkr).

In the **Code** tab you will find a code that is missing a single character in
order to pass the tests. However, your goal is to submit a function as
**minimalist** as possible. Use the tips in the tips section below.

Write a function that returns the boolean `True` if the given number is
**zero** , the string `"positive"` if the number is **greater than zero** or
the string `"negative"` if it's **smaller than zero**.

### Tips

Executing a `return` will effectively **end your function**.

For example, the code:

    def compare_to_100(x):
        if x > 100:
            return "greater"
        elif x < 100:
            return "smaller"
        else:
            return "equal"

Can be simplified to:

    def compare_to_100(x):
        if x > 100:
            return "greater"
        if x < 100:
            return "smaller"
        return "equal"

  * If `x` is greater than 100, Python will not execute the code past the first `return`.
  * If `x` is smaller than 100, Python will not execute the code inside the first if statement or past the second `return`.
  * If `x` is equal to 100, Python will not execute the code inside the two if statements.
  * This can **only** be used if you have a `return` inside your if statement.

### Bonus

Further simplification of the code above:

    def compare_to_100(x):
        return "greater" if x > 100 else "smaller" if x < 100 else "equal"

### Notes

  * This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your **suggestions** in the **Comments**.
  *  _ **Readability**_ is indeed a subjective concept. **Let's discuss it!** Feel free to leave your opinion in the **Comments**.
  * You can find all the exercises in this series [over here](https://edabit.com/collection/8F3LA2Mwrf5bp7kse).

"""

def equilibrium(x):
  return "positive" if x>0 else "negative" if x<0 else True

