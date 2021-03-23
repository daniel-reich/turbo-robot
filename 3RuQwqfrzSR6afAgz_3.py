"""


In **Rail Fence Cipher** encoding is done by by placing each character
successively in a diagonal along a set of **rails**.

Create a function that takes two arguments; a string and the number of rails,
and returns the **encoded message**.

    message = "WEAREDISCOVEREDFLEEATONCE"
    rails = 3
    
    rail_fence_cipher(message, rails) ➞ "WECRLTEERDSOEEFEAOCAIVDEN"

In above example, given message to be decomposed in 3 rails:

    W       E       C       R       L       T       E
      E   R   D   S   O   E   E   F   E   A   O   C
        A       I       V       D       E       N

Starting from upper line, encoded message will be :

    "WECRLTEERDSOEEFEAOCAIVDEN"

### Examples

    rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3) ➞ "WECRLTEERDSOEEFEAOCAIVDEN"
    
    rail_fence_cipher("EDABITISAMAZING", 4) ➞ "EIIDTSZNAIAAGBM"
    
    rail_fence_cipher("WEWILLALLDIEONEDAY", 3) ➞ "WLLOAEILLDENDYWAIE"

### Notes

Rails will be >=2

"""

class Rail_Cypher:
​
  
  def __init__(self, rail_num):
    self.rn = rail_num
    self.rails = {n: [] for n in range(self.rn)}
  
  def encrypt(self, msg):
​
    rail = 0
    direct = 'U'
    msg = list(msg)
​
    while len(msg) > 0:
     # print(msg, rail, direct)
      self.rails[rail].append(msg.pop(0))
      if direct == 'U':
        if rail == max(self.rails.keys()):
          direct = 'D'
          rail -= 1
        else:
          rail += 1
      elif direct == 'D':
        if rail == 0:
          direct = 'U'
          rail += 1
        else:
          rail -= 1
    
    return ''.join([''.join(self.rails[rail]) for rail in sorted(self.rails.keys())])
​
def rail_fence_cipher(msg, rails):
​
  rc = Rail_Cypher(rails)
  return rc.encrypt(msg)

