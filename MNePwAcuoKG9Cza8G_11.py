"""


Create a function that builds a staircase given the height and the type of
building block.

### Examples

    build_staircase(3, "#") ➞ [
      ["#", "_", "_"],
      ["#", "#", "_"],
      ["#", "#", "#"]
    ]
    
    build_staircase(4, "#") ➞ [
      ["#", "_", "_", "_"],
      ["#", "#", "_", "_"],
      ["#", "#", "#", "_"],
      ["#", "#", "#", "#"]
    ]
    
    build_staircase(3, "A") ➞ [
      ["A", "_", "_"],
      ["A", "A", "_"],
      ["A", "A", "A"]
    ]
    
    # height = 3 and building block = "A"
    
    build_staircase(4, "$") ➞ [
      ["$", "_", "_", "_"],
      ["$", "$", "_", "_"],
      ["$", "$", "$", "_"],
      ["$", "$", "$", "$"]
    ]
    
    # height = 4 and building block = "$"

### Notes

  * If the height is 0, return an empty list `[]`.
  * See **Comments** or **Resources** for help.

"""

def build_staircase(height, block):
  reslt_arry = []
  for i in range(1,height+1):
    tmp_arry = []
    tmp_arry = [block]*i + ['_']*(height-i)
    reslt_arry.append(tmp_arry)
  return reslt_arry

