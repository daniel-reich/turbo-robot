"""


Your job is to make a "Twitter link" regular expression `rx`. This RegEx
searches a tweet to find the **@handle** and the **#handle**. Only return the
**@** and **#** handles.

### Examples

    tweet("Visit us at @edabit") ➞ "@edabit"
    
    tweet("Follow @JavaScript") ➞ "@JavaScript"
    
    tweet("#Honesty is the best @policy!!") ➞ "#Honesty @policy"

### Notes

Make sure the RegEx doesn't return `.` `,` `!` `?`, etc.

"""

def tweet(txt):
    import re
    solution = ""
    
    HandlesRegex = re.compile(r'(^|\s)(@|#)(\w*)')
    matches = HandlesRegex.findall(txt)
​
    for space, handle, text in matches:
        if len(solution) == 0:
            solution += handle+text
        elif len(solution) > 0:
            solution += ' '+handle+text
    return solution

