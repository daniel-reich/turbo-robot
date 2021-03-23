"""


Check the principles of minimalist code in the [intro to the first
challenge](https://edabit.com/challenge/2XLjgZhmACph76Pkr).

In the **Code** tab you will find a code that is missing a single character in
order to pass the tests. However, your goal is to submit a function as
**minimalist** as possible. Use the tips in the tips section below.

Write a function that returns `True` if the given positive integer is a
**prime number** and `False` if it's not.

### Tips

Everything you writer **after** `if`, `not`, `while` or **around** `and`,
`or`, `is`, `in` is interpreted as a boolean.

A function that prints a **countdown** from the absolute value of `x` and
prints also `"hey"` if the number is a multiple of `3` and contains the digits
`"3"`, could be written as:

    def countdown(x):
        if x < 0:
            x = x * -1
        while x > 0:
            if x % 3 == 0:
                if "3" in str(x):
                    print(x)
                    print("hey")
            else:
                print(x)
            x = x - 1

This can be simplified to:

    def countdown(x):
        x = abs(x)
        while x:
            print(x)
            if not x % 3 and "3" in str(x):
                print("hey")
            x -= 1

  * `abs()` gets the absolute value of a number.
  * `while` will interpret `x` as a boolean, [exiting the loop after reaching zero](https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/).
  * `print(x)` needs to be called whether `x` is a "hey number" or not. This can be done outside of any `if` statement, instead of in both.
  * Both conditions `x % 3 == 0` and `"3" in str(x)` need to be `True`, so they can be joined with an `and`.

### Bonus

A more Pythonistic approach:

    def countdown(x):
        for i in range(abs(x), -1, -1):
            print(x)
            if not x % 3 and "3" in str(x):
                print("hey")

### Notes

  * This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your **suggestions** in the **Comment tab**.
  *  _ **Readability**_ is indeed a subjective concept. **Let's discuss it!** Feel free to leave your opinion in the **Comments tab**.
  * You can find all the exercises in this series [over here]().

"""

def is_prime(n):
  if n == 0:
    return False
  if n == 1:
    return False
  i = 2
  while i < n:
    if n % i == 0:
      return False
    i += 1
  return True

