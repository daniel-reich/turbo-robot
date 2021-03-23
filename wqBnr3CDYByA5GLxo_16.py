"""


Write a function that takes in a string and returns all possible combinations.
Return the final result in **alphabetical order**.

### Examples

    unravel("a[b|c]") ➞ ["ab", "ac"]
    
    unravel("a[b|c]de[f|g]") ➞ ["abdef", "acdef", "abdeg", "acdeg"]
    
    unravel("a[b]c[d]") ➞ ["abcd"]
    
    unravel("a[b|c|d|e]f") ➞ ["abf", "acf", "adf", "aef"]
    
    unravel("apple [pear|grape]") ➞ ["apple grape", "apple pear"]

### Notes

Think of each element in every block (e.g. `[a|b|c]`) as a **fork in the
road**.

"""

def unravel(txt):
  def find_changeables(txt):
​
    l = list(txt)
​
    changeable_indexes = []
    current_index = []
​
    for n in range(0, len(l)):
      item = l[n]
​
      if item == '[':
        if current_index == []:
          current_index = [n]
        else:
          return 'Current Index Error: n = {}, ci = {}'.format(n, current_index)
      elif item == ']':
        if current_index != [] and len(current_index) == 1:
          current_index.append(n + 1)
          changeable_indexes.append(current_index)
          current_index = []
        else:
          return 'Current Index Error: n = {}, ci = {}'.format(n, current_index)
    
    if current_index != []:
      if len(current_index) == 1:
        current_index.append(len(l))
        changeable_indexes.append(current_index)
  
      else:
        return 'Current Index Error: ci = {}'.format(current_index)
    
    del current_index
​
    changeables = {}
​
    for pair in changeable_indexes:
​
      startn = int(pair[0])
      endn = int(pair[1])
​
      key = txt[startn:endn]
      value = key.strip('[').strip(']').split('|')
​
      changeables[key] = value
    
    return changeables
  def format_txt(txt, changeables):
​
    new_text = []
​
    keys = list(changeables.keys())
​
    total_possibilities = 1
    for key in keys:
      v = changeables[key]
      l = len(v)
      total_possibilities *= l
    
​
    for n in range(0, total_possibilities):
      new_text.append(txt)
    
​
    for n in range(0, len(keys)):
      key = keys[n]
      choices = changeables[key]
​
      c = 0
      l = len(choices)
      n = 0
      cc = 0
​
      while cc < total_possibilities:
        while c < l:
        
          item = new_text[n]
          choice = choices[c]
​
          item = item.replace(key, choice)
          new_text[n] = item
          c += 1
          cc += 1
          n += 1
        c = 0
​
      new_text = sorted(new_text)
    return sorted(new_text)
​
  fc = find_changeables(txt)
  ft = format_txt(txt, fc)
  
  return ft

