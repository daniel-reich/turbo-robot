"""


For each challenge of this series you **do not** need to submit a function.
Instead, you need to submit a **template string** that can be formatted in
order to get a certain outcome.

Write a template string according to the following example:

### Example

    a = "John"
    b = "Joe"
    c = "Jack"
    template = "yourtemplatestringhere"
    template.format(a, b, c) ➞ "Their names were: John, Joe and Jack."

### Tips

A **template string** is a string that uses curly braces `{}` as a placeholder
that can then be formatted:

    "hello, my name is {}".format("John") ➞ "hello, my name is John."

Do not put any value inside `{}`.

### Notes

  * Submit a string, not a function.
  * Do not change the name of the variable `template`.
  * You can find all the exercises in this series [over here](https://edabit.com/collection/hCYFNwxGwnAYzq497).

"""

template = "Their names were: {}, {} and {}."
a = "John"
b = "Joe"
c = "Jack"
template.format(a, b, c)

