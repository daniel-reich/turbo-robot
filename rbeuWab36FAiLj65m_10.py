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
  def cap_count(words):
    
    cc = {}
​
    for word in words: 
      c = 0
​
      for l8r in word:
        t = l8r.isupper()
​
        if t == True:
          c += 1
      
      key = c
      v = word
​
      if key not in cc.keys():
        cc[key] = [v]
      else:
        cc[key].append(v)
  
    ncc = {}
​
    for key in sorted(cc.keys()):
      v = cc[key]
      v.sort()
      ncc[key] = v
    
    return ncc
  def lexicon_order(value):
    
    conversions = {}
    nv = []
​
    for v in value:
      nv.append(v.lower())
      conversions[v.lower()] = v
    
    nv.sort()
​
    tr = []
​
    for item in nv:
      tr.append(conversions[item])
    
    return tr
​
  cc = cap_count(w)
  tr = {}
​
  for key in cc.keys():
    
    v = cc[key]
​
    nv = lexicon_order(v)
​
    tr[key] = nv
  
  return tr

