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
    if sort == 'prefix':
        files = [i.split('.') for i in files]
        filename = [i[0] for i in files]
        uniquefilename = []
        final = []
        for i in filename:
            if i not in uniquefilename:
                uniquefilename.append(i)
        print(uniquefilename)
        for i in range(len(uniquefilename)):
            final.append([])
            for j in files:
                if uniquefilename[i] in j:
                    final[i].append('.'.join(j))
        return final
            
    if sort == 'suffix':
        files = [i.split('.') for i in files]
        filename = [i[1] for i in files]
        uniqueext = []
        final = []
        for i in filename:
            if i not in uniqueext:
                uniqueext.append(i)
        for i in range(len(uniqueext)):
            final.append([])
            for j in files:
                if uniqueext[i] in j:
                    final[i].append('.'.join(j))
        return final

