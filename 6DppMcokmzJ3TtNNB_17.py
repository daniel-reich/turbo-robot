"""


Create a function which takes every letter in every word, and puts it in
alphabetical order. Note how the **original word lengths must stay the same**.

### Examples

    true_alphabetic("hello world") ➞ "dehll loorw"
    
    true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"
    
    true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"

### Notes

  * All sentences will be in lowercase.
  * No punctuation or numbers will be included in the **Tests**.

"""

import re
​
def true_alphabetic(txt):
    length = [len(word) for word in txt.split()]
    order_txt = "".join(sorted(re.sub(r" ", "", txt)))
    print(order_txt)
    start = 0
    result = ""
    end = 0
    for num in length:
        end += num
        result += order_txt[start:end] + " "
        start += num
    return result.rstrip()

