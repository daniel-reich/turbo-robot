"""


As you know, the function `range()` returns a range of numbers, but it doesn't
work on alphabets. In this challenge, we try to fill this gap.

Write a function `alpha-range()` which takes three arguments `start`, `stop`,
and `step` (which its default value is one). The function must return a list
of alphabetical characters, ranging from start character to stop character
based on `step` value.

The function must follow these conditions:

  * If `step` is zero or more than 26 or less than -26, return `"step must be a non-zero value between -26 and 26, exclusive"`.

  * Both `start` and `stop` must share the same case, otherwise, return `"both start and stop must share the same case"`.

Like `range()` function:

  * `step` must not be zero.

Unlike `range()` function:

  * returned list must be inclusive.
  * the order of characters doesn't affect the output (i.e. the output of `alpha_range("a", "f")` is the same as `alpha_range("f", "a")`, see examples).

### Examples

    alpha_range("a", "f") ➞ ["a", "b", "c", "d", "e", "f"]
    
    alpha_range("f", "a") ➞ ["a", "b", "c", "d", "e", "f"]
    
    alpha_range("a", "f", -1) ➞ ["f", "e", "d", "c", "b", "a"]
    
    alpha_range("f", "a", -1) ➞ ["f", "e", "d", "c", "b", "a"]
    
    alpha_range("A", "F", -1) ➞ ["F", "E", "D", "C", "B", "A"]
    
    alpha_range("A", "F", 0) ➞ "step must be a non-zero value between -26 and 26, exclusive"
    
    alpha_range("A", "F", -26) ➞ "step must be a non-zero value between -26 and 26, exclusive"
    
    alpha_range("a", "F", -1) ➞ "both start and stop must share the same case"

### Notes

All the `start` and `stop` values in the tests are valid alphabetical
characters.

"""

def alpha_range(start, stop, step=1):
    if step < -26 or step > 26 or step == 0:
        return "step must be a non-zero value between -26 and 26, exclusive"
    elif ((start.isupper() and stop.islower()) or
          (start.islower() and stop.isupper())):
        return "both start and stop must share the same case"
    b, e = ord(start), ord(stop)
    if (e < b and step > 0) or (step < 0 and b < e):
        b, e = e, b
    return [chr(i) for i in range(b, e + (1 if step > 0 else -1), step)]

