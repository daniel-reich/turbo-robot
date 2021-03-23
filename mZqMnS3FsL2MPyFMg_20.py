"""


Write a function that accepts a positive integer between `0` and `999`
inclusive and returns a string representation of that integer written in
English.

### Examples

    num_to_eng(0) ➞ "zero"
    
    num_to_eng(18) ➞ "eighteen"
    
    num_to_eng(126) ➞ "one hundred twenty six"
    
    num_to_eng(909) ➞ "nine hundred nine"

### Notes

  * There are no hyphens used (e.g. "thirty five" not "thirty-five").
  * The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

"""

def num_to_eng(n):
    eng=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen',\
         'fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','','','twenty','thirty','forty','fifty',\
         'sixty','seventy','eighty','ninety']
    d=e=f=g=0
    s=''
    d=n%100
    e=n//100
    f=d%10
    g=d//10
    if e:
        s+=eng[e]+' '+'hundred '
    if g>1:
        s+=eng[g+20]+' '+eng[f]
    else:
        s+=eng[d]
    if s=='':
        s='zero'
    return s

