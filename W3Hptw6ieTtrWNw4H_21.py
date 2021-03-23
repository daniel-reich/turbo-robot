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
    enc_flag = False
    for ele in text:
        if not ele.isalpha():
            enc_flag = True
            break
    coding_list = [chr(i) for i in range(ord('a'),ord('z')+1) if i != ord('j')]
    coding_table = {e:(i//5, i%5) for i,e in enumerate(coding_list)}
    coding_table_inverse = {coding_table[i]:i for i in coding_table}
    if enc_flag:
        new_text = ''.join([i.lower() for i in text if i.isalpha()])
        result_code_list = []
        for e in new_text:
            e = e.lower()
            if e == 'j':
                e = 'i'
            result_code_list.append(coding_table[e])
        temp_list = [e[i] for i in range(2) for e in result_code_list]
        result = ''.join([coding_table_inverse[(temp_list[i], temp_list[i+1])] for i in range(0, len(temp_list), 2)])
    else:
        result_code_list = []
        for e in text:
            code = coding_table[e]
            result_code_list.append(code[0])
            result_code_list.append(code[1])
        temp_list = []
        length = len(result_code_list)
        for i in range(length//2):
            temp_list.append(result_code_list[i])
            temp_list.append(result_code_list[i+length//2])
        result = ''.join([coding_table_inverse[(temp_list[i], temp_list[i+1])] for i in range(0, len(temp_list), 2)])
            
    return result

