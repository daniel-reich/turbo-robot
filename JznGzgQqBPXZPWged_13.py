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

def se(lst):
    s = 0
    for i in lst:
        s+=i
    return s
def par(lst):
    s = 0
    for i in lst:
        if i !=0:
            s+=1/i
    return round((1/s),1)
def Mod(net):
    r = ""
    for e in net:
        if e=="(":
            r+= "se(["
        elif e==")":
            r+= "])"
        elif e=="[":
            r+="par(["
        elif e=="]":
            r+="])"
        else:
            r+=e
    return r
def resist(net):
    m_net = Mod(net)
    return eval(m_net)

