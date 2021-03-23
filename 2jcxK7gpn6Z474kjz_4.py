"""


You're head of security at a casino that has money being stolen from it. You
get the data in the form of strings and you have to set off an alarm if a
thief is detected.

  * If there is no guard between thief and money, return `"ALARM!"`
  * If the money is protected, return `"Safe"`

### String Components

  * x - Empty Space
  * T - Thief
  * G - Guard
  * $ - Money

### Examples

    security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"
    
    security("xxTxxG$xxxx$xxxx") ➞ "Safe"
    
    security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"

### Notes

Money at the extremes are safe.

"""

def security(txt):
    if txt[0] == "$":
        return "ALARM!!"
    for i in range(len(txt)):
        if txt[i] == "$":
            index_guard_before = txt.rfind("G", 0, i)
            index_theif_before = txt.rfind("T", 0, i)
            index_guard_behind = txt.find("G", i, len(txt) + 1)
            index_theif_behind = txt.find("T", i, len(txt) + 1)
            if index_guard_before == -1 and index_theif_before != -1:
                return "ALARM!"
            elif index_guard_before != -1 and index_theif_before != -1 and index_guard_before < index_theif_before:
                return "ALARM!"
            elif index_guard_behind == -1 and index_theif_behind != -1:
                return "ALARM!"
            elif index_guard_behind != -1 and index_theif_behind != -1 and index_guard_behind > index_theif_behind:
                return "ALARM!"
​
    return "Safe"

