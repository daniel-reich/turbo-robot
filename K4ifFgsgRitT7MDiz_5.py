"""
For each challenge of this series you **do not** need to submit a function.
Instead, you need to submit a **template string** that can formatted in order
to get a certain outcome.

Write a template string according to the following example. Notice the period
`.` at the end of the strings:

### Example

    template = "yourtemplatestringhere"
    template.format("name", "Johnny", "$", "<", 10)) ➞ "My name is: Johnny$$$$."

### Tips

The content of a placeholder can be formatted dynamically by positional or
keyword arguments:

    "{:{align}{width}.{length}}.".format("Peter", align=">", width=5, length=2) ➞ "   Pe."

### Notes

  * Submit a string, not a function.
  * Do not change the name of the variable `template`.
  * You can find all the exercises in this series [over here](https://edabit.com/collection/hCYFNwxGwnAYzq497).

"""

template = "My {} is: {:{}{}{}s}."

