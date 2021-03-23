"""


 **Mubashir** needs your help to learn Python Programming. Help him by
modifying a given string `txt` as follows:

  * Reverse the string given.
  * Replace each letter to its position in the alphabet for example (a = 1, b = 2, c = 3, ...).
  * Join the array and convert it to a number.
  * Convert the number to binary.
  * Convert the string back to a number.

See below example for more understanding :

 **modify("hello") ➞ 111001101011101101101010**

     "hello" = "olleh"
     
     "olleh" = ['15', '12', '12', '5', '8']
     
     ['15', '12', '12', '5', '8'] = 15121258
     
     15121258 = "111001101011101101101010"
     
     "111001101011101101101010" = 111001101011101101101010

### Examples

    modify("hello") ➞ 111001101011101101101010
    
    modify("mubashir") ➞ 10110000110010000110011111000111000001
    
    modify("edabit") ➞ 111111110110001110001

### Notes

There are no spaces and the string is lowercase.

"""

def modify(txt):
    lst_idx = [c for c in range(ord('a')-96, ord('z')-95)]
    lst_ch = [chr(c) for c in range(ord('a'), ord('z')+1)]
    lst_zip = list(zip(lst_ch, lst_idx))
    lst_pos = []
    for ch in txt[::-1]:
        for elem in lst_zip:
            if elem[0] == ch:
                lst_pos.append(elem[1])
                break
    num = int(''.join(list(map(str, lst_pos))))
    num_bin = str(bin(num))[2:]
    return int(num_bin)

