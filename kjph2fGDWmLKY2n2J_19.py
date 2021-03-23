"""


Given an RGB(A) CSS color, determine whether its format is valid or not.
Create a function that takes a string (e.g. `"rgb(0, 0, 0)"`) and return
`True` if it's format is correct, otherwise return `False`.

### Examples

    valid_color("rgb(0,0,0)") ➞ True
    
    valid_color("rgb(0,,0)") ➞ False
    
    valid_color("rgb(255,256,255)") ➞ False
    
    valid_color("rgba(0,0,0,0.123456789)") ➞ True

### Notes

  * Alpha is between 0 and 1.
  * There are a few edge cases (check out the **Tests** tab to know more).

"""

def valid_color (color):
  parts_index=0
  correct_parts=0
  print(color)
  if color[0:4] == "rgb(":
    parts_index = 4
  elif color[0:5] == "rgba(":
    parts_index = 5
  else:
    return(False)
  if color[-1] != ")":
    return(False)
  parts_str=color[parts_index:-1].replace(" ","").replace(" ","")
  if (parts_str.index(",") > 0):
    parts_list=parts_str.split(",")
    if len(parts_list) == 3 and parts_index == 4:
      for part in parts_list:
        if len(part) > 0 and (part.isnumeric()) and int(part) == float(part) and (int(part) in range(0,256)):
          correct_parts += 1
        elif len(part) > 0 and part[-1] == "%" and int(part[0:-1]) == float(part[0:-1]) and (int(part[0:-1]) in range(0,101)):
          correct_parts += 1
        else:
          return(False)
    elif len(parts_list) == 4 and parts_index == 5:
      for part in parts_list[0:3]:
        if len(part) > 0 and (part.isnumeric()) and int(part) == float(part) and (int(part) in range(0,256)):
          correct_parts += 1
        elif len(part) > 0 and part[-1] == "%" and int(part[0:-1]) == float(part[0:-1]) and (int(part[0:-1]) in range(0,101)):
          correct_parts += 1
        else:
          return(False)
      if len(parts_list[-1]) > 0 and "." in parts_list[-1]:
        if (float(parts_list[-1]) < 0.0) or (float(parts_list[-1]) > 1.0):
          print("False: " + str(float(parts_list[-1])))
          return(False)
        else:
          correct_parts += 1
      else:
        if len(parts_list[-1]) == 0 or not(parts_list[-1].isnumeric()) or (float(parts_list[-1]) < 0.0) or (float(parts_list[-1]) >= 256.0):
          print("False: " + str(float(parts_list[-1])))
          return(False)
        else:
          correct_parts += 1
    else:
      return(False)
  print(str(correct_parts))
  if correct_parts == parts_index - 1:
    return(True)
  else:
    return(False)

