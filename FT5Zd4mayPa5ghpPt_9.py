"""


Create a function that converts RGB to HEX and vice versa.

`color_conversion("#ff09d3")` converts the string param from HEX to RGB.
`color_conversion({"r": 235, "g": 64, "b": 52})` converts the dict param from
RGB to HEX.

### Examples

    color_conversion("#ffffff") ➞ {"r": 255, "g": 255, "b": 255}
    
    color_conversion("#ff0025") ➞ {"r": 255, "g": 0, "b": 37}
    
    color_conversion({"r": 40, "g": 200, "b": 125}) ➞ "#28c87d"
    
    color_conversion({"r": -1, "g": 0, "b": 256}) ➞ "Invalid input!"
    
    color_conversion("c9bade") ➞ {"r": 201, "g": 186, "b": 222}

### Notes

  * The **_RGB_** value must be between 0 and 255.
  * Hex value input can be prefixed with a hash (`#`) or without (see example #5).

"""

def color_conversion(h):
  return hex_to_dec(h) if isinstance(h,str) else dec_to_hex(h)
  
def hex_to_dec(s):
  if not all([i in '0123456789abcdef#' for i in s]) or len(s.replace('#',''))>=7:
    return 'Invalid input!'
  s = ''.join([i for i in s if i in '0123456789abcdef'])
  dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
  ret = {'r':s[0:2],'g':s[2:4],'b':s[4:6]}
  for i in ret:
    ret[i] = dic[ret[i][0]]*16+dic[ret[i][1]]
  return ret
    
def dec_to_hex(d):
  if not all([0<=d[i]<=255 for i in d]):
    return 'Invalid input!'
  lst = list('0123456789abcdef')
  ret = '#'
  for i in ['r','g','b']:
    ret+=lst[d[i]//16]+lst[d[i]%16]
  return ret

