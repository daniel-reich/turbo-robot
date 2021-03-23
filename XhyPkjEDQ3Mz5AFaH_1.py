"""


Given an input string `s` and a pattern `p`, implement regular expression
matching with support for "." and "*" .

### Examples

    is_match("aa", "a") ➞ false
    # "a" does not match the entire string "aa".
    
    is_match("aa", "a*") ➞ true
    # "*" means zero or more of the preceding element, "a".
    # Therefore, by repeating "a" once, it becomes "aa".
    
    is_match("ab", ".*") ➞ true
    # ".*" means "zero or more (*) of any character (.)".

### Notes

  * `s` could be empty and contains only lowercase letters a-z.
  * `p` could be empty and contains only lowercase letters a-z, and characters like . or *.

"""

def is_match(s,p):
    if not p:
        return not s
    i, dp = 0, {0}
    while i < len(p):
        matches, c = set(), p[i]
        if i < len(p) - 1 and p[i + 1] == '*':
            if c == '.':
                dp = set(range(min(dp), len(s) + 1))
            else:
                for length in dp:
                    matches.add(length)
                    while length < len(s) and s[length] == c:
                        length += 1
                        matches.add(length)
                dp = matches
            i += 2
        else:
            if c == '.':
                dp = {length + 1 for length in dp if length < len(s)}
            else:
                for length in dp:
                    if length < len(s) and s[length] == c:
                        matches.add(length + 1)
                dp = matches
            i += 1
        if not dp:
            return False
​
    return len(s) in dp

