"""


For each challenge of this series you **do not** need to submit a function.
Instead, you need to submit a **template string** that can formatted in order
to get a certain outcome.

Write a three templates string according to the following example. All final
strings must have a length of 20 characters:

### Example

    starry = "yourtemplatestringhere"
    dash = "yourtemplatestringhere"
    money = "yourtemplatestringhere"
    
    starry.format("Starry") ➞ "*******Starry*******"
    dash.format("Dash") ➞ "----------------Dash"
    money.format("Money") ➞ "Money$$$$$$$$$$$$$$$"

### Tips

You can pad a string with a placeholder in the format `{:cdx}` where `c` is
the padding character, `d` is one of three directions (`<`, `^` or `>`) and
`x` is the width.

For example:

    "Best score{:->15}".format('AAA') ➞ "Best score------------AAA"

### Notes

  * Submit a string, not a function.
  * Do not change the name of the variables `starry`, `dash` and `money`.
  * You can find all the exercises in this series [over here](https://edabit.com/collection/hCYFNwxGwnAYzq497).

"""

starry = "{:*^20}"
dash = "{:->20}"
money = "{:$<20}"
​
starry.format("Starry")
dash.format("Dash") 
money.format("Money")

