"""


You can assign variables from lists like this:

    first, _ , last = [1, 2, 8]
    
    first   = lst[0]
    
    _   = ignores second value (2)
    
    last   = lst[-1]
    
    print(first) ➞ outputs 1
    print(last) ➞ outputs 8

Using **Destructuring Assignment** (check the **Resources** tab), your task is
to unpack the list `writeyourcodehere` into three variables, `first`, **a
variable to ignore all middle values** and `last`.

### Notes

  * Your solution should be just **One Line** code.
  * If your solution is longer than one line of code, please check the **Resources** tab.
  * Another version of [this challenge](https://edabit.com/challenge/YWoJkmMHYEENCvgRP).

"""

writeyourcodehere = [1, 2, 3, 4, 5, 6, 7, 8]
first = (writeyourcodehere[0])
last = (writeyourcodehere[-1])

