"""


Resistors are electrical components that add resistance to a circuit.
Resistance is measured in ohms. When resistors are connected in series, the
total resistance is merely the sum of the individual resistances:

    Rtotal = R1 + R2 + R3 + ...

When resistors are connected in parallel, the reciprocal of the total
resistance is equal to the sum of the reciprocals of the individual
resistances:

    1/(Rtotal) = 1/R1 + 1/R2 + 1/R3 + ...

Let's specify that series resistors be designated by enclosing them in
parentheses, and parallel resistors by enclosing them in square brackets. Now
we can calculate the equivalent resistance of the network:

  * `(2, 3, 6)` = 11 ohms
  * `[2, 3, 6]`= 1 ohm

Nesting these structures in the same way tuples and lists are nested allows us
to model complex resistor networks.

Create a function that takes a nested network as a string and returns the
equivalent resistance of the network. Round results to the nearest tenth of an
ohm.

### Examples

    resist("(10, [20, 30])") ➞ 22.0
    # 10 in series with [20, 30] in parallel.
    
    resist("[10, (20, 30)]") ➞ 8.3
    # 10 in parallel with (20, 30) in series.
    
    resist("([10, 20], (30, 40))") ➞ 76.7
    # [10, 20] in parallel in series with (30, 40) in series.
    
    resist("(1, [12, 4, (1, [10, (2, 8)])])") ➞ 3.0
    
    resist("(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])") ➞ 10

### Notes

This is the schematic for the last example above:

![](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/resistor-
res54.gif)

"""

def resist(net):
  import re
  out1=re.sub(', ','+',str(net))
  out=''
  p_count=0
  s_count=0
  serial=False
  parallel=False
  string_counter=0
  for i in out1:
    if i =='[':
      if (parallel):
        if(s_count==0):
          out+='('
        else:
          out+='1/'+ '('
      else:
        if p_count==0:
          out+='1/'+ '('
          parallel=True
        else:
          out+='('
          parallel=True
      p_count+=1
      num_num=0
      last_bracket='['
    
    if i=='(':
      serial=True
      s_count+=1
      num_num=0
      last_bracket='('
      if (parallel):
        out+='1/'+ i
      else:
        out+=i
    
    if i==']':
      p_count -=1
      if p_count==0:
        parallel=False
      num_num=0
      out+=')'
      if s_count>0:
        last_bracket='('
    
    if i==')':
      s_count -=1
      if s_count==0:
        serial=False
      num_num=0
      out+=i
      if p_count>=s_count:
        last_bracket='['
    
    if i=='+':
      out1+=i
      num_num=0
      out+=i
    
    if i.isnumeric():
      if (parallel and not serial):
        if (num_num==0 and s_count==0):
          out+='1/' +i
        else:
          out+=i
        num_num+=1
      
      if (serial and not parallel):
        out+=i
      
      if (serial and parallel and last_bracket=='('):
        out+=i
      
      if (serial and parallel and last_bracket=='['):
        if num_num==0 and p_count>=s_count:
          out+='1/' +i
        else:
          out+=i
        num_num+=1
        
    string_counter+=1
​
  return round(eval(out),1)

