"""


Create a function that returns the number of characters shared between two
words.

### Examples

    shared_letters("apple", "meaty") ➞ 2
    # Since "ea" is shared between "apple" and "meaty".
    
    shared_letters("fan", "forsook") ➞ 1
    
    shared_letters("spout", "shout") ➞ 4

### Notes

N/A

"""

def shared_letters(txt1, txt2):
​
    n=len(txt2)
​
    lista=[]
​
    for i in range(0,n):
        if txt2[i] in txt1:
            lista.append(txt2[i])
​
    return len(lista)
​
​
shared_letters("spout", "shout")

