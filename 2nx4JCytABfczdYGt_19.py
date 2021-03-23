"""


In this challenge, you must build a function that inflects an infinitive
regular Italian verb of the first conjugation form to the present tense,
including the personal subjective pronoun.

All first conjugation Italian verbs share the same suffix: **ARE**. The first
thing to do is separate the verb root from the suffix.

  * Root of "programmare" ( _to code_ ) = "programm".
  * Root of "giocare" ( _to play_ ) = "gioc".

For each subjective pronoun the root is combined with a new suffix: see table
below (pronouns are numbered for coding ease, in real grammar they are grouped
in singular and plural, both from first to third):

#| Pronoun| Suffix  
---|---|---  
1| Io ( _I_ )| o  
2| Tu ( _You_ )| i  
3| Egli ( _He_ )| a  
4| Noi ( _We_ )| iamo  
5| Voi ( _You_ )| ate  
6| Essi ( _They_ )| ano  
  
  * Present tense of verb "parlare" ( _to speak_ ) for third pronoun:
    * Pronoun ("Egli") + Root ("parl") + Suffix ("a") = "Egli parla".
  * Present tense of verb "lavorare" ( _to work_ ) for fourth pronoun:
    * Pronoun ("Noi") + Root ("lavor") + Suffix ("iamo") = "Noi lavoriamo".

There are two exceptions for present tense inflection:

  * If root ends with " **c** " or " **g** " the second and fourth pronoun suffixes add a " **h** " at the start:
    * "Attaccare" ( _to attack_ ) = "Tu attacchi" (instead of _"Tu attacci"_ )
    * "Legare" ( _to tie_ ) = "Noi leghiamo" (instead of _"Noi legiamo"_ )
  * If root ends with " **i** " the second and fourth pronoun suffixes lose the starting " **i** " (so that second pronoun suffix disappears):
    * "Inviare" ( _to send_ ) = "Noi inviamo" (instead of _"Noi inviiamo"_ )
    * "Tagliare" ( _to cut_ ) = "Tu tagli" (instead of _"Tu taglii"_ )
    * "Mangiare" ( _to eat_ ) = "Noi mangiamo" (instead of _"Noi mangiiamo"_ )
    * "Cacciare" ( _to hunt_ ) = "Tu cacci" (instead of _"Tu caccii"_ )

Given a string `verb` being the infinitive form of the first conjugation
Italian regular verb, and an integer `pronoun` being the subjective personal
pronoun, implement a function that returns the inflected form as a string.

### Examples

    conjugate("programmare", 5) ➞ "Voi programmate"
    
    conjugate("iniziare", 2) ➞ "Tu inizi"
    
    conjugate("mancare", 4) ➞ "Noi manchiamo"

### Notes

  * In the returned string, pronouns must be capitalized and verbs must be in lowercase, separated by a space between them.
  * Curious fact: first conjugation (verbs ending in "are") is also called "the living conjugation", because every new verb that enters the Italian dictionary is assigned to this category as a new regular verb; it often happens for verbs "borrowed" from English and for informatical neologisms: _chattare_ , _twittare_ , _postare_ , _spammare_... will _edabittare_ be the next?

"""

def conjugate(verb, pronoun):
  verb = verb.replace("are", "")
  if pronoun == 1:
    verb = "Io " + verb + "o"
  if pronoun == 2:
    if verb[-1] == "i":
      verb = "Tu " + verb
    elif verb[-1] == "c" or verb[-1] == "g":
      verb = "Tu " + verb + "hi"
    else:
      verb = "Tu " + verb + "i"
  if pronoun == 3:
    verb = "Egli " + verb + "a"
  if pronoun == 4:
    if verb[-1] == "i":
      verb = "Noi " + verb + "amo"
    elif verb[-1] == "c" or verb[-1] == "g":
      verb = "Noi " + verb + "hiamo"
    else:
      verb = "Noi " + verb + "iamo"
  if pronoun == 5:
    verb = "Voi " + verb + "ate"
  if pronoun == 6:
    verb = "Essi " + verb + "ano"
​
  return verb

