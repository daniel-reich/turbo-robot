"""


Create a function that converts Celsius to Fahrenheit and vice versa.

### Examples

    convert("35*C") ➞ "95*F"
    
    convert("19*F") ➞ "-7*C"
    
    convert("33") ➞ "Error"

### Notes

  * Round to the nearest integer.
  * If the input is incorrect, return `"Error"`.
  * For the formulae to convert back and forth, check the **Resources** tab.

"""

def convert(deg):
  print (deg)
  print (deg[-2::])
  
  if deg[-2::]!="*C" and deg[-2::]!="*F":
    print ("nope")
    return "Error"
  elif deg[-2::]=="*C":
    temp=int(deg[0:-2:])
    
    temp*=1.8
    temp+=32
    print (temp)
    
    return str(round(temp))+"*F"
    
  
  else: 
    temp=int(deg[0:-2:])
    print ("degrees=",temp)
    temp-=32
    temp/=1.8
    print (temp)
    return str(round(temp))+"*C"

