"""


Create a function that, given a list of string lists, returns an list of all
combinations as concatenated strings.

  1. The function is called with a list of lists containing strings.
  2. The task is to combine each string of each array with each string of each other list.
  3. If one of the string lists is empty, the function will return an empty list.

The function will accept an optional second string parameter. This parameter,
if specified, is to be used to combine two strings.

### Examples

    combinator([["a", "b"], ["c", "d"]]) ➞ ["ac", "ad", "bc", "bd"]
    
    combinator([["a"], ["a", "b"], "abc"]) ➞ ["aaa", "aab", "aac", "aba", "abb", "abc"]
    
    combinator([["foo", "bar"], ["baz", "bamboo"]], " ") ➞ ["foo baz", "foo bamboo", "bar baz", "bar bamboo"]
    
    combinator([[]]) ➞ []

### Notes

  * The order of the given strings must be retained in the combinations.
  * You can assume that:
    * The function is always called with a list of string lists and lists can be empty.

"""

def combinator(lst, string = None):
  if len(lst) == 1:
    return lst[0]
  
  if string != None:
    tr = []
    
    if len(lst) == 2:
      a, b = lst
      
      if [] in [a, b]:
        return []
        
      for item in a:
        for itm in b:
          tr.append(item + string + itm)
    
    if len(lst) == 3:
      a, b, c = lst
      
      if [] in [a, b, c]:
        return []
      
      for item in a:
        for itm in b:
          for it in c:
            tr.append(string.join([item, itm, it]))
    
    return tr
  if len(lst) == 2:
    a, b = lst
    
    if a == [] or b == []:
      return []
    
    tr = []
    
    for item in a:
      for itm in b:
        tr.append(item + itm)
  
  if len(lst) == 3:
    a, b, c = lst
    
    if a == [] or b == []:
      return []
    
    tr = []
    
    for item in a:
      for itm in b:
        for it in c:
          tr.append(item + itm + it)
  
  return tr

