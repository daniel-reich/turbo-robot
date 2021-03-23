"""


You are in the midst of organizing all of your coding projects. It's a mess!
Every file you've ever created is located in the same folder.

To clean it up, you've decided that you will use one of two organization
methods.

  1. The `prefix` method: You will group all files with the same project name under the same folder.
  2. The `suffix` method: You will group all files with the same extension under the same folder.

Create a function that takes in the current folder sorts the files according
to the organization method (`prefix` or `suffix`). A folder is a grouping of
files in the same list.

### Examples

    # Sorting by project name (ex1 and ex2)
    clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "prefix") ➞ [
      ["ex1.html", "ex1.js"],
      ["ex2.html", "ex2.js"]
    ]
    
    # Sorting by extension (.html and .js)
    clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "suffix") ➞ [
      ["ex1.html", "ex2.html"],
      ["ex1.js", "ex2.js"]
    ]
    
    clean_up(["music_app.js", "music_app.png", "music_app.wav", "tetris.png", "tetris.js"], "prefix") ➞ [
      ["music_app.js", "music_app.png", "music_app.wav"],
      ["tetris.png", "tetris.js"]
    ]
    
    clean_up(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "suffix") ➞ [
      ["_1.rb", "_2.rb", "_3.rb", "_4.rb"]
    ]
    
    clean_up(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "prefix") ➞ [
      ["_1.rb"], ["_2.rb"],
      ["_3.rb"], ["_4.rb"]
    ]

### Notes

Keep elements in the same relative order.

"""

def clean_up(files, sort):
  l=[]
  ml=[]
  e=[]
  p=""
  s=""
  c=0
  switch=True
  if sort=="prefix":
    for f in files:
      for x in f:
        if x==".":
          break
        else:
          p=p+x
      if p not in e:
        e.append(p)
        l.append(f)
        ml.append(l)
        l=[]
        p=""
      else:
        for m in ml:
          for d in m:
            for q in d:
              if q==".":
                break
              else:
                s=s+q
            if p==s:
              m.append(f)
              s=""
              p=""
              switch=False
              break
            else: 
              s=""
          if switch==False:
            switch=True
            break
    return ml
  elif sort=="suffix":
    for f in files:
      for x in range(len(f)):
        if f[x]==".":
          p=p+f[x+1:]
      if p not in e:
        e.append(p)
        l.append(f)
        ml.append(l)
        l=[]
        p=""
      else:
        for m in ml:
          for d in m:
            for q in range(len(d)):
              if d[q]==".":
                s=s+d[q+1:]
            if p==s:
              m.append(f)
              s=""
              p=""
              switch=False
              break
            else:
              s=""
          if switch==False:
            switch=True
            break
    return ml

