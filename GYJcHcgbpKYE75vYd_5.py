"""


Create a function that takes an integer and returns it as an **ordinal
number**. An Ordinal Number is a number that tells the position of something
in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.

### Examples

    return_end_of_number(553) ➞ "553-RD"
    
    return_end_of_number(34) ➞ "34-TH"
    
    return_end_of_number(1231) ➞ "1231-ST"
    
    return_end_of_number(22) ➞ "22-ND"
    
    return_end_of_number(412) ➞ "412-TH"

### Notes

Check the **Resources** tab for more info on _ordinal numbers_.

"""

def return_end_of_number(num):
  
  if (num == 1):
    return "1-ST"
  elif (num == 2):
    return "2-ND"
  elif (num == 3):
    return "3-RD"
  elif (num >= 4) and (num <= 9):
    return str(num) + "-TH"
  
  elif (str(num)[-1] == "1") and (str(num)[-2] == "1"):
    return str(num) + "-TH"
  elif (str(num)[-1] == "1") and (str(num)[-2] != "1"):
    return str(num) + "-ST"
  
  elif (str(num)[-1] == "2") and (str(num)[-2] == "1"):
    return str(num) + "-TH"
  elif (str(num)[-1] == "2") and (str(num)[-2] != "1"):
    return str(num) + "-ND"
  
  elif (str(num)[-1] == "3") and (str(num)[-2] == "1"):
    return str(num) + "-TH"
  elif (str(num)[-1] == "3") and (str(num)[-2] != "1"):
    return str(num) + "-RD"
  
  else:
    return str(num) + "-TH"

