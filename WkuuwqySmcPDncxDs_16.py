"""


For each challenge of this series you **do not** need to submit a function.
Instead, you need to submit a **template string** that can formatted in order
to get a certain outcome.

Write a template string according to the following example. All final strings
must have a length of 20 characters:

### Example

    template = "yourtemplatestringhere"
    template.format(fname = "John", lname = "Doe") ➞ "JoDo###############."

### Tips

The placeholder `{:.x}` will truncate a string at index x:

    "My initial is {:.1}.".format("Edabit") ➞ "My initial is E."

### Notes

  * Sumbit a string, not a function.
  * Do not change the name of the variable `template`.
  * You can find all the exercises in this series [over here](https://edabit.com/collection/hCYFNwxGwnAYzq497).

"""

template = "{fname:2.2}{lname:#<17.2}."

