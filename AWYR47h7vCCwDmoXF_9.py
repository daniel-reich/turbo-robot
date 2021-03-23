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

def is_goal_scored(arrays):
    goal_definition, ball_location, counter = [], [], 0
    for array in arrays:
        for i in range(0,len(list(array[0])),1):
            if list(array[0])[i] == "#" and len(goal_definition) < 2:
                goal_definition.append(i)
            if list(array[0])[i] == "0":
                ball_location.append(counter)
                ball_location.append(i)
        counter +=1
    return True if ball_location[1] > goal_definition[0] and ball_location[1] < goal_definition[1] and ball_location[0] <= 2 else False

