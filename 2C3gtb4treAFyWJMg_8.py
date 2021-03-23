"""


The **Polybius Square** cipher is a simple substitution cipher that makes use
of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and
"J" typically sharing a slot (as there are 26 letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
To encipher a message, each letter is merely replaced by its row and column
numbers in the grid.

Create a function that takes a plaintext or ciphertext message, and returns
the corresponding ciphertext or plaintext.

### Examples

    polybius("Hi") ➞ "2324"
    
    polybius("2324  4423154215") ➞ "hi there"
    
    polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"

### Notes

  * As "I" and "J" share a slot, both are enciphered into 24, but deciphered only into "I" (see third and fourth test).
  * Any charactor other than letters and spaces should be dropped from the cypher.

"""

convert_txt = [
    ['A','B','C','D','E'],
    ['F','G','H','I/J','K'],
    ['L','M','N','O','P'],
    ['Q','R','S','T','U'],
    ['V','W','X','Y','Z']
    ]
​
def is_number(text):
    return [i for i in text if i >= '0' and i <= '9']
​
def polybius(text):
    test_str = ''
    temp_txt = ''
    r_list = []
    
    if (len(is_number(text)) != 0):
        for i in text:
            if i == ' ':
                test_str += ' '
            else:
                temp_txt += i
                if int(temp_txt) >= 10 and int(temp_txt) <= 99 :
                    if convert_txt[int(temp_txt[0]) - 1][int(temp_txt[1]) - 1] == 'I/J':
                        test_str += 'I'
                    else:
                        test_str += convert_txt[int(temp_txt[0]) - 1][int(temp_txt[1]) - 1]
                    temp_txt = ''
        return test_str.lower()
    else:
        for i in text.upper():
            if ( i == ' '):
                r_list += [' ']
            else:
                for m in range(0,len(convert_txt)):
                    for n in range(0,len(convert_txt[m])):
                        if i in convert_txt[m][n] :
                            r_list += [str(m + 1) + str(n + 1) ]
        return ''.join(r_list)

