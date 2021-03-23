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

def unique(lst):
  for item in lst:
    while lst.count(item) > 1:
      lst.remove(item)
  return lst
  
def clean_up(files, criteria):
  split_files = []
  for f in files:
    split_files.append( f.split('.') )
    
  prefixes = []
  suffixes = []
  subgroup = []
  output = []
  
  for f in split_files:
    prefixes.append(f[0])
    suffixes.append(f[1])
  prefixes = unique(prefixes)
  suffixes = unique(suffixes)
  
  if criteria == 'prefix':
    for p in prefixes:
      for item in split_files:
        if item[0] == p:
          subgroup.append( '.'.join(item) )
      output.append(subgroup)
      subgroup = []
  
  else:
    for s in suffixes:
      for item in split_files:
        if item[1] == s:
          subgroup.append( '.'.join(item) )
      output.append(subgroup)
      subgroup = []
  return output

