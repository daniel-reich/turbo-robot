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
    z = sorted([f(x) for x in w])
    d = {}
    for c, l, wd in z:
        if c not in d:
            d[c] = []
        d[c].append(wd)
    return d
    
def f(x):
    cnt = 0
    for ch in x:
        if ch.isupper():
            cnt += 1
    return (cnt, x.lower(), x)

