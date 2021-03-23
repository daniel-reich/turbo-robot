"""


Create a function that takes a multidimensional list and returns the total
count of numbers in that list.

### Examples

    count_number([["", 17.2, 5, "edabit"]]) ➞ 2
    # 17.2 and 5.
    
    count_number([[[[[2, 14]]], 2, 3, 4]]) ➞ 5
    # 2, 14, 2, 3 and 4.
    
    count_number([["number"]]) ➞ 0

### Notes

Input may be a list of numbers, strings and empty lists.

"""

def count_number(lst):
  
  Text = str(lst)
  Text = Text.replace("[","")
  Text = Text.replace("]","")
  Text = Text.replace("'","")
  Text = Text.replace(" ","")
  
  Blocks = Text.split(",")  
  
  Events = 0
  
  Counter = 0
  Length = len(Blocks)
  
  while (Counter < Length):
    
    Item = Blocks[Counter]
        
    if (Item == ""):
      Counter += 1
    
    elif (Item.isdigit()):
      Events += 1
      Counter += 1
    
    elif ("." in Item):
      First = str(Item[0])
            
      if (First.isdigit()):
        Events += 1
        Counter += 1
    
      else:
        Counter += 1
                
    else:
      Counter += 1
  
  return Events

