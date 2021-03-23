"""


A night club will give you a word. For entrance, you need to provide the right
number according to the provided word.

Every given word will have a doubled letter, like "dd" in addiction. To answer
the right number you need to find the doubled letter's position in the
alphabets and multiply this number with 4.

Create a function that takes the argument of `word` and returns the right
number.

### Examples

    club_entry("hill") ➞ 48
    # 'l' is 12th alphabet
    # 12*4 = 48
    
    club_entry("apple") ➞ 64
    
    club_entry("bee") ➞ 20

### Notes

N/A

"""

import string
​
​
def club_entry(word):
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    numlst=[]
    for i in range(1,27):
        numlst.append(i)
    combined_dict=dict(zip(alphabet_list,numlst))
    for i in word:
        if word.count(i)==2 and word.find(i+i)!=-1:
            return combined_dict[i]*4

