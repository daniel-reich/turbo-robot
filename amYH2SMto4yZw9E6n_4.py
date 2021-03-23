"""


Write a function that returns `True` if the phone number is in a valid format.
Valid formats are as follows:

 **With Country Code**|  **Without Country Code**  
---|---  
+1-892-445-7663| 892-445-7663  
1-892-445-7663| (892) 445-7663  
1 (892) 445-7663| 892.567.8901  
1.892.567.8901| 1/892/567/8901  
1 892 567 8901| 892/567/8901  
18925678901| 892 567 8901  
  
### Examples

    validate("578-332-1114") ➞ True
    
    validate("57-332-1114") ➞ False
    
    validate("577 332  1114") ➞ False
    # More than one space in between digits clusters.
    
    validate("57 332 1114") ➞ False
    # Unacceptable digit cluster length.
    
    validate("157%332-1114") ➞ False
    # Unacceptable delimiter.

### Notes

  * The country code will always be `+1` or `1`.
  * Each phone number will contain either 10 or 11 digits (depending on whether the country code exists).
  * There must either be exactly one space, a delimiter, or no space at all between the digit clusters.
  * You do not have to worry about extensions.

"""

def validate(phone_number):
  phone_number_list = list(phone_number)
​
  digits = '0123456789'
  separators = '+-()./ '
​
  brackets = False
​
  num_digits = 0
  for digit in digits:
    num_digits += phone_number_list.count(digit)
​
  print(phone_number_list)
​
  if((num_digits != 10) and (num_digits != 11)):
    return False
​
  for char in phone_number_list:
    if(char not in digits+separators):
      return False
​
  if((phone_number_list[0] == "+") and (phone_number_list[1] =="1")): # if regional code +1
    if(phone_number_list[2] not in digits):
      phone_number_list = phone_number_list[3:]
    else:
      phone_number_list = phone_number_list[2:]
​
  elif((phone_number_list[0] == "1") and (num_digits == 11)): # if regional code 1
    if(phone_number_list[1] not in digits):
      phone_number_list = phone_number_list[2:]
    else:
      phone_number_list = phone_number_list[1:]
​
  elif(num_digits != 10):
    return False
​
  print(phone_number_list)
​
  if((phone_number_list[0] == "(")):
    if(phone_number_list[4] != ")"):
      return False
​
    phone_number_list.pop(4)
    phone_number_list.pop(0)
​
    brackets = True
​
  print(phone_number_list)
​
  if(len(phone_number_list) == 10):
    return True
​
  elif(len(phone_number_list) == 12):
    if(brackets and (phone_number_list[3] == " ") and (phone_number_list[7] == "-")):
      return True
​
    elif((phone_number_list[3] == phone_number_list[7]) and (phone_number_list[3] not in digits)):
      return True
      
    else:
      return False
​
  else:
    return False

