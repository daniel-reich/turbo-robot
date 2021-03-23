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
  b="ACBDEFGHIJKLMNOPQRSTUVQXYZ"
  l=[]
  d={}
  q={}
  c=0
  a=[]
  for e in w:
    for r in e:
      if r in b:
        c+=1
    if c in d.keys():
      d[c]=d[c]+[e]
    else:
      d[c]=[e]
    c=0
  for k in d.keys():
    l.append(k)
  l.sort()
  for v in l:
    x=list(d[v])
    for y in range(len(x)):
      x[y]=x[y].lower()
    x.sort()
    for y in x:
      for j in d[v]:
        if j.lower()==y:
          a.append(j)
    q[v]=a
    a=[]
  return q

