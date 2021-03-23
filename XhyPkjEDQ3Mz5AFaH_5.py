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

def is_match(s, p):
  def star_format(string, goal):
    if '*' not in string:
      return string
    else:
      
      ns = ''
      pi = None
      non_stars = [item for item in string if item != '*']
      for item in string:
        if pi == None:
          pi = item
          ns += item
        elif item == '*':
          for n in range(len(goal) - len(non_stars)):
            ns += pi
        else:
          pi = item
          ns += item
      print(ns)
      return ns
  def dot_format(string):
    return '.' in string
  
  sf = star_format(p,s)
  df = dot_format(p)
  
  if df == True:
    return df
  print(sf)
  return sf == s

