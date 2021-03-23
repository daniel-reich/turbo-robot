"""


A **named capturing group** will match "x" in `(?P<name>x)` and will store the
match under the name `name`.

Let's see an example. To extract the United States area code from a phone
number, we could use:

    txt = "(214) 987-6482"
    m = re.match("\((?P<area>\d{3})\)", txt)
    
    m.group("area") ➞ 214

Write a **regular expression** to match the year, month and day in a string.
Store the matches in three groups named **year** , **month** and **day**
respectively. All strings will be given in the following format `YYYY-MM-DD`.

### Example

    txt = "2020-04-18"
    pattern = "yourregularexpressionhere"
    m = re.search(pattern, txt)
    
    m.group("year") ➞ "2020"
    m.group("month") ➞ "04"
    m.group("day") ➞ "18"

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and named capturing groups in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"

