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

def grouping(w):
  group = {}
  for word in w:
    n = sum(c.isupper() for c in word)
    if n not in group:
      group[n] = []
    group[n].append(word)
  return {k:sorted(v, key = lexi) for k,v in group.items()}
  
def lexi(w):
  return [ord(c) for c in w.lower()]

