"""


For each challenge of this series you **do not** need to submit a function.
Instead, you need to submit a **template string** that can be formatted in
order to get a certain outcome.

Write a template string according to the following example:

### Example

    a = "John"
    b = "Joe"
    template = "yourtemplatestringhere"
    
    template.format(a, b) ➞ "Joe hit John and then John hit Joe."

### Tips

Writing a number n inside a place holder will tell `.format()` to fill in with
the nth argument. For example:

    "{0} said: Hi, I'm {0}.".format("Monica") ➞ "Monica said: Hi, I'm Monica."

### Notes

  * Submit a string, not a function.
  * Do not change the name of the variable `template`.
  * You can find all the exercises in this series [over here](https://edabit.com/collection/hCYFNwxGwnAYzq497).

"""

template = "yourtemplatestringhere"
c = "John"
a = "Joe"
template = "{1} hit {0} and then {0} hit {1}."
template.format(a,c)

