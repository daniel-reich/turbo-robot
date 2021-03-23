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

import re
def clean_up(files, sort):
​
  seen = []
  results = []
​
  if sort == 'prefix':
​
    for idx, value in enumerate([re.search('[A-Za-z0-9]+', x).group() for x in files]):
​
      if idx == 0:
        seen.append(value)
        results.append([files[idx]])
​
      if value in seen and idx != 0:
        results[ [re.search('[A-Za-z0-9]+', x[0]).group() for x in results].index(value) ] += [files[idx]]
​
      elif value not in seen and idx != 0:
        seen.append(value)
        results.append([files[idx]])
​
    return results
​
​
  if sort == "suffix":
​
    for idx, value in enumerate([re.findall(r'[.](.+)', x)[0] for x in files]):
​
      if idx == 0:
        seen.append(value)
        results.append([files[idx]])
​
      if value in seen and idx != 0:
        results[ [re.findall(r'[.](.+)', x[0])[0] for x in results].index(value) ] += [files[idx]]
​
      elif value not in seen and idx != 0:
        seen.append(value)
        results.append([files[idx]])
​
    return results

