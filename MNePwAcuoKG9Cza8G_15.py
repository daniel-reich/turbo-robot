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
  output = [] 
  for i in range(height):
    current_row = []
    for c in range(i+1):
      current_row.append(block)
    for c in range(i+1, height):
      current_row.append('_')
    output.append(current_row)
    
  return output

