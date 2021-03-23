"""


You're given a 2D list / matrix of a crop field. Each crop needs a water
source. Each water source hydrates the 8 tiles around it. With `"w"`
representing a water source, and `"c"` representing a crop, is every crop
hydrated?

### Examples

    crop_hydrated([
      [ "w", "c" ],
      [ "w", "c" ],
      [ "c", "c" ]
    ]) ➞ True
    
    crop_hydrated([
      [ "c", "c", "c" ]
    ]) ➞ False
    # There isn"t even a water source.
    
    crop_hydrated([
      [ "c", "c", "c", "c" ],
      [ "w", "c", "c", "c" ],
      [ "c", "c", "c", "c" ],
      [ "c", "w", "c", "c" ]
    ]) ➞ False

### Notes

`"w"` on its own should return `True`, and `"c"` on its own should return
`False`.

"""

def crop_hydrated(field):
  length=len(field)
  width=len(field[0])
  flag=True
  
  def check(x, i):
    try:
      if(field[x+1][i]=="w"):
        print('test1')
        return True
    except:
      pass
      
    try:
      if(field[x-1][i]=="w" and (x-1)>=0):
        print('test2')
        return True
    except:
      pass
      
    try:
      if(field[x][i+1]=="w"):
        print('test3')
        return True
    except:
      pass
      
    try:
      if(field[x][i-1]=="w" and (i-1)>=0):
        print('test4')
        return True
    except:
      pass
      
    try:
      if(field[x+1][i+1]=="w"):
        print('test5')
        return True
    except:
      pass
      
    try:
      if(field[x-1][i-1]=="w" and (x-1)>=0 and (i-1)>=0):
        print('test6')
        return True
    except:
      pass
      
    try:
      if(field[x+1][i-1]=="w" and (i-1)>=0):
        print('test7')
        return True
    except:
      pass
      
    try:
      if(field[x-1][i+1]=="w" and (x-1)>=0):
        print('test8')
        return True
    except:
      pass
      
  for x in range(len(field)):
    for i in range(len(field[x])):
      if(field[x][i]=="c"):
        if(check(x, i)):
          continue
        else:
          print('error')
          flag=False
  return flag

