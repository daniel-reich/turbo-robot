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

### returns polybius square reference for a given letter
def polybius(letter):
  n = ord(letter) - 97
  if n > 8:
    n -= 1
  return [n//5 + 1, n%5 + 1]
​
### main function
def bifid(txt):
  ### encryption
  if " " in txt:
    ### prepare plaintext
    txt = "".join(char for char in txt.lower().replace("j","i") if char.isalpha())
    
    ### get polybius square row and column values 
    rows, columns = [], []
    for letter in txt:
      value = polybius(letter)
      rows.append(value[0])
      columns.append(value[1])
    
    ### scramble values
    num_lst = rows + columns
    letter_codes = [[num_lst[i],num_lst[i+1]] for i in range (0,len(num_lst),2)]
  
  ### decryption  
  else:
    ### get polybius values
    num_lst = []
    for letter in txt:
      num_lst += polybius(letter)
    
    ### unscramble values
    n = len(num_lst)//2
    letter_codes = [[num_lst[i],num_lst[i+n]] for i in range (n)]
  
  ### get output text
  output = ""
  for code in letter_codes:
    n = (code[0]-1) * 5 + code[1] + 96
    if n > 105:
      n += 1
    output += chr(n)
  
  return output

