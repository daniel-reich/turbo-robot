"""


Create a function which **replaces** all instances of `"nts"` with `"nce"` and
**vice versa** if they are at the _end of a word_.

### Examples

    switcheroo("The elephants in France were chased by ants!") ➞ "The elephance in Frants were chased by ance!"
    
    switcheroo("While he rants, I fall into a trance...") ➞ "While he rance, I fall into a trants..."
    
    switcheroo("Bounced over the fence!") ➞ "Bounced over the fents!"

### Notes

  * Empty strings should return just an empty string (see example #2).
  * Ignore punctuation and any instances where `"nts"` or `"nce"` are not at the end of a word (see example #3).

"""

def switcheroo(txt):
  txt = txt.split(" ")
  for i in range(len(txt)):
      w = "".join([k for k in txt[i] if k.isalpha()])
      if "nts" in w:
          if w[-3:] == "nts":
              txt[i] = txt[i].replace("nts", "nce")
      elif "nce" in w:
          if w[-3:] == "nce":
              txt[i] = txt[i].replace("nce", "nts")
  return " ".join(txt)

