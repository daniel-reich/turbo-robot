"""


Create a function that takes a string as the first argument, and a (string)
specification as a second argument. If the specification is `"word"`, return a
string with each word reversed while maintaining their original order. If the
specification is `"sentence",` reverse the order of the words in the string,
while keeping the words intact.

### Examples

    txt = "There's never enough time to do all the nothing you want"
    flip("Hello", "word") ➞ "olleH"
    
    flip("Hello", "sentence") ➞ "Hello"
    
    flip(txt, "word") ➞ "s'erehT reven hguone emit ot od lla eht gnihton uoy tnaw"
    
    flip(txt, "sentence") ➞ "want you nothing the all do to time enough never There's"

### Notes

N/A

"""

def flip(txt, spec):
    words = txt.split(" ")[::-1]
    words_reversed = txt.split(" ")
    word_result = ""
    sentence_result = ""
    for i in range(0,len(words_reversed)):
        words_reversed[i] = words_reversed[i][::-1]
    if spec == "word":
        for i in words_reversed:
            word_result += i + " "
        return(word_result[:-1])
    elif spec == "sentence":
        for i in words:
            sentence_result += i + " "
    return(sentence_result[:-1])

