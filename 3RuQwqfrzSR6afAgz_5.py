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

def rail_fence_cipher(msg, rails):
    rail_lst = build_rail_sequence(msg, rails)           
    return rail_encrypt(msg, rail_lst)
​
def rail_encrypt(msg, rail_lst):
    cipher = {}
    cipher_txt = ""
    for i in range(max(rail_lst) + 1):
        cipher[i] = ""
    for i in range(len(msg)):
        cipher[rail_lst[i]] += msg[i]
    for v in cipher.values():
        cipher_txt += v
    return cipher_txt
​
def build_rail_sequence(msg, rails):
    char_cnt = 0
    order = []
    down = False
    indx = 0
    while char_cnt < len(msg):
        order.append(indx)
        if indx == rails-1:
            down = True
        elif indx == 0:
            down = False
       
        if down:
            indx -= 1
        else:
            indx += 1
        char_cnt += 1
    return order

