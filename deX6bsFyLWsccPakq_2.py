"""


Write a **regular expression** to find all the times in a string. Times will
be in 24-hours format with hours and minutes and **optionally** seconds:
**hh:mm(:ss)**. Match only valid times.

### Example

    txt1 = "Breakfast at 09:00 in the room 123:456."
    txt2 = "The incident took place last Wednesday at 00:56:41."
    txt3 = "We will have two meetings: from 10:30 to 11:00 and from 11:45 to 11:75."
    pattern = "yourregularexpressionhere"
    
    re.findall(pattern, txt1) ➞ ["09:00"]
    re.findall(pattern, txt2) ➞ ["00:56:41"]
    re.findall(pattern, txt3) ➞ ["10:30", "11:00", "11:45"]

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx in **Resources**.
  * If you're stuck, check **Comments** for some hints.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = r"\s([0-2][0-9](?:\:[0-5][0-9]){1,2})\b(?!\:)"

