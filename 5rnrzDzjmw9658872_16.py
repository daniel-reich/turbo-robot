"""


For each challenge of this series you **do not** need to submit a function.
Instead, you need to submit a **template string** that can be formatted in
order to get a certain outcome.

Write three template strings according to the following example. All final
strings must have a **length of 30 characters**. Notice the **period** `.` at
the end of the strings:

### Example

    name = "John"
    
    left_align = "yourtemplatestringhere"
    center_align = "yourtemplatestringhere"
    right_align = "yourtemplatestringhere"
    
    left_align.format(name) ➞ "My name is John              ."
    center_align.format(name) ➞ "My name is        John       ."
    right_align.format(name) ➞ "My name is               John."

### Tips

The placeholders `{:<x}`, `{:^x}`, `{:>x}` are used to align left, center and
right respectively within a width x.

For example:

    "Credits: {:>7}".format(128) ➞ "Credits:     128"

### Notes

  * Submit a string, not a function.
  * Do not change the name of the variables `left_align`, `center_align`, `right_align`.
  * You can find all the exercises in this series [over here](https://edabit.com/collection/hCYFNwxGwnAYzq497).

"""

left_align = "My name is {:<18}."
center_align = "My name is {:^18}."
right_align = "My name is {:>18}."

