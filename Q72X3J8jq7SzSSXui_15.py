"""


Create a function that returns the whole of the first sentence which contains
a specific word. Include the full stop at the end of the sentence.

### Examples

    txt = "I have a cat. I have a mat. Things are going swell."
    
    sentence_searcher(txt, "have") ➞ "I have a cat."
    
    sentence_searcher(txt, "MAT") ➞ "I have a mat."
    
    sentence_searcher(txt, "things") ➞ "Things are going swell."
    
    sentence_searcher(txt, "flat") ➞ ""

### Notes

  * Sentences will **always** end with full stops.
  * Your function should not be case sensitive.
  * Return an empty string if the word isn't found in the sentence.

"""

def sentence_searcher(txt, word):
    word = word.lower()
    txt1 = txt.split(".")
    res = []
   
    for i in txt1:
        splt = i.split(" ")
        
        for j in splt:
            if j.lower() == word:
                res.append(i.strip() + ".")
            else:
                continue
    if len(res) != 0:
        return res[0]
    else:
        return ""

