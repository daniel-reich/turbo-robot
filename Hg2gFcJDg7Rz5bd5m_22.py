"""


Write a function that takes as input **two different dictionaries** and
filters the **keys in each dictionary** to only keep keys that exist in
**both** dictionaries. Store your result as a list with two dictionaries.

### Examples

    dict1 = {"a": 5, "b": 13, "c": 7}
    dict2 = {"b": 5, "c": 8, "d": 91, "e": 99}
    dict3 = {"a": 1, "b": 34}
    dict4 = {"c": 9, "d": 8}
    
    intersection(dict1, dict2) ➞ [{"b": 13, "c": 7}, {"b": 5, "c": 8}]
    
    intersection(dict1, dict4) ➞ [{"c": 7}, {"c": 9}]
    
    intersection(dict3, dict4) ➞ [{}, {}]

### Notes

If no keys are shared between both dictionaries, return a list of **empty
dictionaries** (see last example).

"""

def intersection(dict1, dict2):
  d3 = {} 
  d4 = {} 
  for k, v in dict1.items():
    if k in dict2:
      d3[k] = v
​
  for k, v in dict2.items():
    if k in dict1:
      d4[k] = v
​
  return [d3, d4]

