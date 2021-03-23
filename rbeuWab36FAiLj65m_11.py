"""


Write a function that groups words by the **number of capital letters** and
returns a dictionary of object entries whose keys are the **number of capital
letters** and the values are the groups.

### Examples

    grouping(["HaPPy", "mOOdy", "yummy", "mayBE"]) ➞ {
      0: ["yummy"],
      2: ["mayBE", "mOOdy"],
      3: ["HaPPy"]
    }
    
    grouping(["eeny", "meeny", "miny", "moe"]) ➞ {
      0: ["eeny", "meeny", "miny", "moe"]
    }
    
    grouping(["FORe", "MoR", "bOR", "tOR", "sOr", "lor"]) ➞ {
      0: ["lor"],
      1: ["sOr"],
      2: ["MoR", "bOR", "tOR"],
      3: ["FORe"]
    }

### Notes

  * The object entries have to be sorted by the **number of capital letters**.
  * The groups will be arrays of all words sharing the same number of capital letters.
  * The groups have to be sorted alphabetically (ignoring case).
  * Words will be unique.

"""

def count_caps(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count
​
def grouping(lst):
    dict = {}
    for word in lst:
        if count_caps(word) in dict:
            dict[count_caps(word)].append(word)
        else:
            dict[count_caps(word)] = [word]
​
    sortedDict = {}
    for k,v in sorted(dict.items()):
        sortedDict[k] = sorted(v, key=lambda x:x.upper())
​
    return sortedDict

