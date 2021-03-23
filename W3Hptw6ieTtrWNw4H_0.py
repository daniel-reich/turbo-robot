"""


The basic **Polybius Square** is a 5x5 square grid with the letters A-Z
written into the grid. "I" and "J" typically share a slot (as there are 26
letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
The **Bifid** cipher uses the Polybius square but adds a layer of complexity.

Start with a secret message. Remove spaces and punctuation.

    plaintext = "ikilledmufasa"

Encipher the message using the basic Polybius cipher (see my [previous
challenge](https://edabit.com/challenge/2C3gtb4treAFyWJMg) — right click and
select "open in new tab"), but write the numbers in two rows under the
message, like so:

i| k| i| l| l| e| d| m| u| f| a| s| a  
---|---|---|---|---|---|---|---|---|---|---|---|---  
2| 2| 2| 3| 3| 1| 1| 3| 4| 2| 1| 4| 1  
4| 5| 4| 1| 1| 5| 4| 2| 5| 1| 1| 3| 1  
  
Read off the numbers horizontally, in pairs:

    22 23 31 13 42 14 14 54 11 54 25 11 31

Generate the ciphertext by converting these new pairs of numbers into new
letters using the Polybius square.

    ciphertext = "ghlcrddyaykal"

Create a function that takes a plaintext or ciphertext, and returns the
corresponding ciphertext or plaintext.

### Examples

    bifid("I killed Mufasa!") ➞ "ghlcrddyaykal"
    
    bifid("ghlcrddyaykal") ➞ "ikilledmufasa"
    
    bifid("hi") ➞ "go"

### Notes

N/A

"""

def bifid(text):
    letters = 'abcdefghiklmnopqrstuvwxyzj'
    codes = ['11', '12', '13', '14', '15', '21', '22', '23', '24', '25',
             '31', '32', '33', '34', '35', '41', '42', '43', '44', '45',
             '51', '52', '53', '54', '55', '24']
    if ' ' in text:
        codes_lst = [codes[letters.index(c.lower())]
                     for c in text if c.isalpha()]
        upper_deck, lower_deck = zip(*codes_lst)
        pairs = ''.join(upper_deck)
        pairs += ''.join(lower_deck)
        return ''.join(letters[codes.index(pairs[i * 2: i * 2 + 2])]
                       for i in range(len(pairs) // 2))
    else:
        codes_str = ''.join(codes[letters.index(c)] for c in text)
        upper_deck = codes_str[:len(codes_str) // 2]
        lower_deck = codes_str[len(codes_str) // 2:]
        codes_lst = [upper_deck[i] + lower_deck[i]
                     for i in range(len(upper_deck))]
        return ''.join(letters[codes.index(c)] for c in codes_lst)

