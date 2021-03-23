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
  for i in goal:
    i = i[0].replace(" ", "")
    if "#0#" in i and not "###" in i: return True
  return False

