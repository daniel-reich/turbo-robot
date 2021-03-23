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
​
  class Color:
​
    def __init__(self, ident, color):
      self.id = ident
      self.color = color
      if self.id == 'RGB':
        self.rgb = color
        self.hex = None
      elif self.id == 'hex':
        if '#' in color:
          self.hex = color
        else:
          self.hex = '#' + color
        self.rgb = None
      else:
        self.rgb = None
        self.hex = None
    
    def convert(self):
      if self.id == 'RGB':
        
        red = h['r']
        green = h['g']
        blue = h['b']
​
        d1 = str(hex(int(red/16)))[2:]
        d2 = str(hex(int(red%16)))[2:]
        d3 = str(hex(int(green/16)))[2:]
        d4 = str(hex(int(green%16)))[2:]
        d5 = str(hex(int(blue/16)))[2:]
        d6 = str(hex(int(blue%16)))[2:]
​
        self.hex = '#{}{}{}{}{}{}'.format(d1,d2,d3,d4,d5,d6)
        return True
      elif self.id == 'hex':
        hexes = '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f'.split(',')
        deces = list(range(0,16))
​
        table = {}
​
        for n in range(16):
          table[hexes[n]] = deces[n]
        
        raw_red = self.hex[1:3]
        raw_green = self.hex[3:5]
        raw_blue = self.hex[5:]
​
        rr2 = []
        rg2 = []
        rb2 = []
​
        for item in raw_red:
          rr2.append(str(table[item]))
        for item in raw_green:
          rg2.append(str(table[item]))
        for item in raw_blue:
          rb2.append(str(table[item]))
        
        red = (int(rr2[1]) * (16 ** 0)) + (int(rr2[0]) * (16 ** 1))
        green = (int(rg2[1]) * (16 ** 0)) + (int(rg2[0]) * (16 ** 1))
        blue = (int(rb2[1]) * (16 ** 0)) + (int(rb2[0]) * (16 ** 1))
        
        self.rgb = {'r': red, 'g': green, 'b': blue}
        return True
      else:
        return False
​
    def valid(self):
      for val in self.rgb.values():
        if val < 0 or val > 255:
          return False
      if len(self.hex) != 7:
        return False
      return True
​
    def print(self, to_print):
      if to_print == 'RGB':
        return self.rgb
      elif to_print == 'hex':
        return self.hex
      else:
        return 'Unknown thing to print!! Unknown: {}'.format(to_print)
​
  ident = None
  find = None
  if isinstance(h, dict) == True:
    ident = 'RGB'
    find = 'hex'
  else:
    ident = 'hex'
    find = 'RGB'
​
  c = Color(ident,h)
  
  try:
    c.convert()
  except KeyError:
    return 'Invalid input!'
    
  if c.valid() == True:
    return c.print(find)
  else:
    return "Invalid input!"

