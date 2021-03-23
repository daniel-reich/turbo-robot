"""


Create a function that takes a string (without spaces) and a word list,
cleaves the string into words based on the list, and returns the correctly
spaced version of the string (a sentence). If a section of the string is
encountered that can't be found on the word list, return `"Cleaving stalled:
Word not found"`.

### Examples

    word_list = ["about", "be", "hell", "if", "is", "it", "me", "other", "outer", "people", "the", "to", "up", "where"]
    cleave("ifitistobeitisuptome", word_list) ➞ "if it is to be it is up to me"
    
    cleave("hellisotherpeople", word_list) ➞ "hell is other people"
    
    cleave("hellisotterpeople", word_list) ➞ "Cleaving stalled: Word not found"

### Notes

Words on the `word_list` can appear more than once in the string. The
`word_list` is a reference guide, kind of like a dictionary that lists which
words are allowed.

"""

def cleave(string, lst):
    lst=sorted(lst,key=len,reverse=True)
    max_count=[string.count(x) for x in lst]
    i=0
    dict1={}
    while(i<max(max_count)):
        for x in lst:
            if x in string and len(x)>1:
                y=[x,string.find(x)]
                dict1[string.find(x)]=x
                string=string[:string.find(x)+len(x)].replace(string[string.find(x):(string.find(x)+len(x))],'1234567890'[:len(x)])+string[string.find(x)+len(x):]
        i+=1
    i=0
    while(i<max(max_count)):
        for x in lst :
            if x in string:
                y=[x,string.find(x)]
                dict1[string.find(x)]=x
                string=string[:string.find(x)+len(x)].replace(string[string.find(x):(string.find(x)+len(x))],'1234567890'[:len(x)])+string[string.find(x)+len(x):]
        i+=1          
    l1=[dict1[x] for x in sorted(dict1)]
    if len("".join(l1))==len(string):
        return (" ".join(l1))    
    else:
        return ("Cleaving stalled: Word not found")

