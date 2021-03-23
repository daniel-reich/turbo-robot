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

def rail_fence_cipher(message, rails):
    rows = [""] * rails
    rows[0] += message[0]
    idx = 1
    n = len(message)
    while idx < n:
        for row in range(1, rails):
            rows[row] += message[idx]
            idx += 1
            if idx == n:
                break
        for row in range(rails - 2, -1, -1):
            if idx == n:
                break
            rows[row] += message[idx]
            idx += 1
    return ''.join(rows)

