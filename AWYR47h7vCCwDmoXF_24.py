"""


In (American) Football, a team can score if they manage to kick a ball through
the goal (i.e. above the crossbar and between the uprights).

Create a function that returns `True` if the ball `0` goes through the goal.
You will be given a list of lists.

### Examples

    is_goal_scored([
      ["  #     #  "],
      ["  #  0  #  "],
      ["  #     #  "],
      ["  #######  "],
      ["     #     "],
      ["     #     "],
      ["     #     "]
    ]) ➞ True
    
    is_goal_scored([
      ["  #0    #  "],
      ["  #     #  "],
      ["  #     #  "],
      ["  #######  "],
      ["     #     "],
      ["     #     "],
      ["     #     "]
    ]) ➞ True
    
    is_goal_scored([
      ["  #     #  "],
      ["  #     #  "],
      ["  #     # 0"],
      ["  #######  "],
      ["     #     "],
      ["     #     "],
      ["     #     "]
    ]) ➞ False

### Notes

  * All goals will be of the same size.
  * All lists will be of equal length (11).
  * A team can never score if it hits the crossbar or goes underneath it.

"""

def is_goal_scored(goal):
  
  Counter = 0
  Length = len(goal)
  
  Failsafe = 0  
  Horizontal = 0
  
  # Establishing Position of Horizontal Bar
  
  while (Counter < Length) and (Failsafe == 0):
    
    Item = str(goal[Counter])
    Test = Item.count("#")
    
    if (Test > 2):
      Horizontal = Counter
      Failsafe += 1
      Counter += 1
    else:
      Counter += 1
  
  # Establishing if Zero is in between Vertical Bars
  
  Counter = 0
  End = Horizontal
  
  while (Counter < End):
    
    Item = str(goal[Counter])
    
    if ("0" in Item):
      Aspect_A = Item.index("#")
      Aspect_B = Item.rindex("#")
      Aspect_C = Item.index("0")
      
      if (Aspect_C > Aspect_A) and (Aspect_C < Aspect_B):
        return True
      else:
        return False
    
    else:
      Counter += 1
  
  return False

