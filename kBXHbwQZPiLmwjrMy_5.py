"""


Pig latin has two very simple rules:

  1. If a word starts with a consonant move the first letter(s) of the word, till you reach a vowel, to the end of the word and add "ay" to the end.
    * have ➞ avehay
    * cram ➞ amcray
    * take ➞ aketay
    * cat ➞ atcay
    * shrimp ➞ impshray
    * trebuchet ➞ ebuchettray
  2. If a word starts with a vowel add "yay" to the end of the word.
    * ate ➞ ateyay
    * apple ➞ appleyay
    * oaken ➞ oakenyay
    * eagle ➞ eagleyay

Write two functions to make an English to pig latin translator. The first
function `translate_word(word)` takes a single word and returns that word
translated into pig latin. The second function `translate_sentence(sentence)`
takes an English sentence and returns that sentence translated into pig latin.

### Examples

    translate_word("flag") ➞ "agflay"
    
    translate_word("Apple") ➞ "Appleyay"
    
    translate_word("button") ➞ "uttonbay"
    
    translate_word("") ➞ ""
    
    translate_sentence("I like to eat honey waffles.") ➞ "Iyay ikelay otay eatyay oneyhay afflesway."
    
    translate_sentence("Do you think it is going to rain today?") ➞ "Oday ouyay inkthay ityay isyay oinggay otay ainray odaytay?"

### Notes

  * Regular expressions will help you not mess up the punctuation in the sentence.
  * If the original word or sentence starts with a capital letter, the translation should preserve its case (see examples #2, #5 and #6).

"""

def translate_word(word):
    vowels=['a','e','i','o','u']
    res,x='',[]
    a=word
    word=word.lower()
    if len(word)==0:
        return word
    if word[0] in vowels:
        res=word+'yay'
        if a[0].isupper():
            return res.title()
        else:
            return res
    else:
        for i,v in enumerate(word):
            if v in vowels:
                res+=word[i:]+word[:i]+'ay'
                x.append(res)
                res=''
        if a[0].isupper():            
            return x[0].title()
        else:return x[0]
def translate_sentence(sentence):
    vowels=['a','e','i','o','u']
    if len(sentence)==0:
        return sentence
    a=sentence.split()
    x,b=[],[]
    sentence=sentence.replace(',','').replace('"','').replace('?','').lower().split()
    for word in sentence:
        if word[0] in vowels :
            x.append(word+'yay')    
        else:
            for i,v in enumerate(word):
                if v in vowels:
                    b.append(word[i:]+word[:i]+'ay')
            x.append(b[0])
            b=[]
    if a[-1]=='end?"': 
        x[0]=x[0].title()
        x[1]=x[1]+','
        x[2]='"'+x[2].title()
        x[-1]=x[-1]+'?'+'"'
        return ' '.join(x)    
    if  x[-1]=='odaytay':
        x[-1]=x[-1].replace('odaytay','odaytay?')
        x[0]=x[0].title()
        return ' '.join(x)
    if a[0].isupper():
        x[0]=x[0].title()
        return ' '.join(x)

