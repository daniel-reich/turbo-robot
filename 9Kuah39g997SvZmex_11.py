"""


Create a function that takes in a sentence as input and returns the **most
common last vowel** in the sentence as a single character string.

### Examples

    common_last_vowel("Hello World!") ➞ "o"
    
    common_last_vowel("Watch the characters dance!") ➞ "e"
    
    common_last_vowel("OOI UUI EEI AAI") ➞ "i"

### Notes

  * There will only be one common last vowel in each sentence.
  * If the word has one vowel, treat the vowel as the last one **even if it is at the start of the word**.
  * The question asks you to compile all of the last vowels of each word and returns the vowel in the list which appears most often.
  *  **y** won't count as a vowel.
  * Return outputs in **lowercase**.

"""

def common_last_vowel(txt):
  
  Sample = txt.lower()
  Blocks = Sample.split(" ")
  
  Passage = ""
  
  Counter = 0
  Length = len(Blocks)
  
  while (Counter < Length):
    
    Word = str(Blocks[Counter])
    Target = -1
    Letter = "a"  
    
    if ("a" in Word):
      
      Test_A = Word.rindex("a")
      
      if (Test_A > Target):
        Target = Test_A
        Letter = "a"
    
    if ("e" in Word):
      
      Test_E = Word.rindex("e")
      
      if (Test_E > Target):
        Target = Test_E
        Letter = "e"
    
    if ("i" in Word):
    
      Test_I = Word.rindex("i")
      
      if (Test_I > Target):
        Target = Test_I
        Letter = "i"
​
    if ("o" in Word):
    
      Test_O = Word.rindex("o")
      
      if (Test_O > Target):
        Target = Test_O
        Letter = "o"
    
    if ("u" in Word):
            
      Test_U = Word.rindex("u")
      
      if (Test_U > Target):
      
        Target = Test_U
        Letter = "u"
    
    Passage = Passage + Letter
    Counter += 1
  
  Highest = -1
  Letter = "a"
  
  Test_01 = Passage.count("a")
  Test_02 = Passage.count("e")
  Test_03 = Passage.count("i")
  Test_04 = Passage.count("o")
  Test_05 = Passage.count("u")
  
  if (Test_01 > Highest):
    Highest = Test_01
    Letter = "a"
  
  if (Test_02 > Highest):
    Highest = Test_02
    Letter = "e"
  
  if (Test_03 > Highest):
    Highest = Test_03
    Letter = "i"
  
  if (Test_04 > Highest):
    Highest = Test_04
    Letter = "o"
  
  if (Test_05 > Highest):
    Highest = Test_05
    Letter = "u"
  
  return Letter

