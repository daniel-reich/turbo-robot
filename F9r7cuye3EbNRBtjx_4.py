"""


The function is given a string with some square brackets in it. You need to
build the outcome string using the rule: `k[substring]` is replaced by the
`substring` inside the square brackets being repeated exactly `k` times.

### Examples

    string_builder("3[a]2[bc]") ➞ "aaabcbc"
    
    string_builder("3[a2[c]]") ➞ "accaccacc"
    
    string_builder("2[abc]3[cd]ef") ➞ "abcabccdcdcdef"

### Notes

`k` is a positive integer.

"""

def string_builder(s): 
    airforce = []
    fan = [] 
    t = ""
    r = ""  
    i = 0
    while i < len(s): 
      count = 0
      if (s[i] >= '0' and s[i] <='9'): 
        while (s[i] >= '0' and s[i] <= '9'): 
          count = count * 10 + ord(s[i]) - ord('0')  
          i += 1
        i -= 1
        airforce.append(count) 
      elif (s[i] == ']'): 
        t = ""  
        count = 0
        if (len(airforce) != 0): 
          count = airforce[-1]  
          airforce.pop() 
        while (len(fan) != 0 and fan[-1] !='[' ): 
          t = fan[-1] + t  
          fan.pop() 
        if (len(fan) != 0 and fan[-1] == '['):  
          fan.pop()  
        for j in range(count): 
          r = r + t  
        for j in range(len(r)): 
          fan.append(r[j])  
        r = "" 
      elif (s[i] == '['): 
        if (s[i-1] >= '0' and s[i-1] <= '9'):  
          fan.append(s[i])
        else: 
          fan.append(s[i])  
          airforce.append(1) 
      else: 
        fan.append(s[i]) 
      i += 1
    while len(fan) != 0: 
      r = fan[-1] + r  
      fan.pop()
    return r

