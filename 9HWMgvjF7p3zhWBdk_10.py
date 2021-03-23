"""


Create a function that takes a dictionary and returns the keys and values as
separate lists. Return the keys sorted alphabetically, and their corresponding
values in the same order.

### Examples

    keys_and_values({ "a": 1, "b": 2, "c": 3 })
    ➞ [["a", "b", "c"], [1, 2, 3]]
    
    keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" })
    ➞ [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]
    
    keys_and_values({ "key1": True, "key2": False, "key3": True })
    ➞ [["key1", "key2", "key3"], [True, False, True]]

### Notes

Remember to sort the keys.

"""

def keys_and_values(d):
  result = []
  result.append([])
  result.append([])
  for key in sorted(d):
    result[0].append(key)
    result[1].append(d[key])
  return result

