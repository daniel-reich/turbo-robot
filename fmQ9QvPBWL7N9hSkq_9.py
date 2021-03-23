"""


Write a function that takes a string, and returns a new string with any
duplicate _consecutive_ letters removed.

### Examples

    unstretch("ppoeemm") ➞ "poem"
    
    unstretch("wiiiinnnnd") ➞ "wind"
    
    unstretch("ttiiitllleeee") ➞ "title"
    
    unstretch("cccccaaarrrbbonnnnn") ➞ "carbon"

### Notes

Final strings _won't_ include words with double letters (e.g. "passing",
"lottery").

"""

def unstretch(word):
    lis = list(word)
    i=0
    j=1
    while j <len(lis):
        if lis[i]==lis[j]:
            lis.pop(j)
            j=i+1
        else:
            i +=1
            j +=1
    result=''
    for char in lis:
        result +=char
    return result

