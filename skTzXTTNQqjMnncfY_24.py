"""


A **non-capturing group** will match "x" in `(?:x)`, however the match won't
be stored, meaning you won't be able to access it using backreference, and it
won't be output separately when using `re.findall()`.

Let's see an example of the difference between capturing and non-capturing
groups:

    txt = "red car, blue car, yellow car, green car, red car, red bike, blue bike"
    
    pattern1 = "(red|blue) car"
    pattern2 = "(?:red|blue) car"
    pattern3 = "red|blue car"
    pattern4 = "((red|blue) (car|bike))"
    pattern5 = "((red|blue) (?:car|bike))"
    re.findall(pattern1, txt) ➞ ["red", "blue", "red"]
    re.findall(pattern2, txt) ➞ ["red car", "blue car", "red car"]
    re.findall(pattern3, txt) ➞ ["red", "blue car", "red", "red"]
    re.findall(pattern4, txt) ➞ [("red car", "red", "car"), ("blue car", "blue", "car"), ("red car", "red", "car"), ("red bike", "red", "bike"), ("blue bike", "blue", "bike")]
    re.findall(pattern5, txt) ➞ [("red car", "red"), ("blue car", "blue"), ("red car", "red"), ("red bike", "red"), ("blue bike", "blue")]

  * The first expression matches either "red" or "blue", as long as they're followed by " car".
  * The second expression matches either "red car" or "blue car".
  * The third expression matches either "red" or "blue car".
  * In the fourth expression matches one of the following possibilities: "red car", "red bike", "blue car", "blue bike". It will return a tuple for each match containing an element for each capturing group, in this case: the whole expression, the color and the vehicle type.
  * The fifth expression is similar to the fourth except the vehicle type is a non-capturing group. As you can see, it is not returned separately.

Write a **regular expression** to match any article + noun pair. The articles
are either "a/an" or "the". Use non-capturing groups in your expression.

### Example

    txt = "There is an apple and a pen on the desk"
    pattern = "yourregularexpressionhere"
    
    re.findall(pattern, txt) ➞ ["an apple", "a pen", "the desk"]

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and non-capturing groups in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
pattern = "(?<![a-z])(?:a|an|the) [a-z]*"

