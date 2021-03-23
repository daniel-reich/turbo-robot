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
    road, r, step = [[] for _ in range(rails)], 0, 1
    for c in message:
        if r == 0:
            step = 1
        elif r == rails - 1:
            step = -1
        road[r].append(c)
        r += step
    return "".join("".join(road[r]) for r in range(rails))

