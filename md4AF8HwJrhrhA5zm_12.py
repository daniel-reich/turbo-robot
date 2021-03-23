"""


In colour theory, colour _harmony_ refers to an aesthetically pleasing
combination of colours. The standard colour wheel shows the 12 primary,
secondary and tertiary colours. Starting with _red_ , and moving clockwise,
the colours are:

    colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]

With an initial colour (called the **anchor** ), you can find combinations of
harmonious colours. The combination types are shown below, for an anchor
colour of _green_ :

![Image of Colour Combinations](https://edabit-
challenges.s3.amazonaws.com/colour_harmony.png)

Given an anchor colour and a combination type, write a function that returns a
_set_ containing all colours within the combination.

### Examples

    colour_harmony("green", "triadic") ➞ { "green", "violet", "orange" }
    
    colour_harmony("blue-green", "complementary") ➞ { "blue-green", "red-orange" }
    
    colour_harmony("orange", "analogous") ➞ { "yellow-orange", "red-orange", "orange" }

### Notes

  * Create the combinations given their relative positions from the anchor colour. For example, the rectangle combination starts with the colours two positions clockwise and four positions anti-clockwise from the anchor (and not the other way around). With the split-complemetary combination, you take the colours five positions both clockwise and anti-clockwise from the anchor. For the analogous combination, you include the colours directly on either side of the anchor.
  * Include the anchor colour in the final set.

"""

def colour_harmony(anchor, combination):
  def combinations(ap, comb):
    def comp(p):
      n = p + 6
​
      if n >= 12:
        n -= 12
      
      return n
    def anal(p):
      m = p - 1
      pl = p + 1
​
      if m < 0:
        m += 12
      if pl >= 12:
        pl -= 12
​
      return [m, pl]
    def tria(p):
      pos = p + 4
      neg = p - 4
​
      if pos >= 12:
        pos -= 12
      if neg < 0:
        neg += 12
      
      return [neg, pos]
    def s_comp(p):
      cp = comp(p)
​
      neg = cp - 1
      pos = cp + 1
​
      if neg < 0:
        neg += 12
      if pos >= 12:
        pos += 12
      
      return neg, pos
    def rect(p):
      def short(p):
        op = p + 2
        return op
      def lon(p):
        l = p + 4
        return l
      
      p2 = short(p)
      p3 = lon(p2)
      p4 = short(p3)
​
      points = [p2, p3, p4]
      np = []
​
      for point in points:
        if point >= 12:
          np.append(point - 12)
        elif point < 0:
          np.append(point + 12)
        else:
          np.append(point)
      
      return np
    def squa(p):
      def side(p):
        return p + 3
      
      sides = [p]
​
      for number in range(0, 3):
        np = side(sides[-1])
        if np >= 12:
          np -= 12
        if np < 0:
          np += 12        
        sides.append(np)
      
      sides.pop(0)
​
      return sides
    
    if comb == 'triadic':
      r = tria(ap)
    elif comb == 'complementary':
      r = comp(ap)
    elif comb == 'square':
      r = squa(ap)
    elif comb == 'analogous':
      r = anal(ap)
    elif comb == 'rectangle':
      r = rect(ap)
    elif comb == 'split_complementary':
      r = s_comp(ap)
    
    return r
  
​
  colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
  colour_idents = range(0, len(colours))
  colour_dic = {}
​
  for number in colour_idents:
    colour = colours[number]
    colour_dic[colour] = number
  
  appos = colour_dic[anchor.lower()]
​
  comb = combinations(appos, combination)
​
  final_colours = set()
​
  final_colours.add(colours[appos])
​
  t = isinstance(comb, int)
​
  if t == False:
    for pos in comb:
      colour = colours[pos]
      final_colours.add(colour)
​
  elif t == True:
    final_colours.add(colours[comb])
  
  return final_colours

