"""


Most Italian verbs fall into one of three categories: those ending in _are_ ,
those ending in _ere_ , and those ending in _ire_. How a verb is inflected
depends on what category it belongs to.

A simple way to inflect an Italian verb is: delete the _are/ere/ire_ ending to
get the verb base, append a part specific to its category, and append a part
common to all verbs. For example, this is the Present Simple of three verbs
for the plural you (Italian _voi_ ):

  * Amare (To love): Voi am **ate** (you love) ➞ Specific: _a_ , common: _te_
  * Credere (To believe): Voi cred **ete** (you believe) ➞ Specific: _e_ , common: _te_
  * Dormire (To sleep): Voi dorm **ite** (you sleep) ➞ Specific: _i_ , common: _te_

Create a function that takes in three parameters and returns an inflected verb
with the appropriate pronoun. The input will be an Italian verb, a person
(first, second, third) and a number (singular, plural).

You'll be given three dictionaries: one with the Italian pronouns, one with
the common part, and one with the specific part. For the first two, the number
will be nested within the person. For the third, you will also find lists as
values for the specific part of verbs ending in _are, ere_ , and _ire_
respectively.

### Examples

    inflect("amare", "first", "pl") ➞ "Noi amiamo"
    # Pronoun: "Noi" + verb base: "am" + specific part: "ia" + common part: "mo"
    
    inflect("credere", "third", "sing") ➞ "Lui/Lei crede"
    # Pronoun: "Lui/Lei" + verb base: "cred" + specific part: "e" + common part: None
    
    inflect("dormire", "sec", "pl") ➞ "Voi dormite"
    # Pronoun: "Voi" + verb base: "dorm" + specific part: "i" + common part: "te"

### Notes

  * The dictionary for the pronouns is called `pronomi`.
  * The dictionary for the specific part is called `verbi_spec`.
  * The dictionary for the common part is called `verbi_com`.
  * You'll find all three in the **Tests** tab of your console. You can copy-paste them on your compiler to work with them, but **don't include them in your submission**.

"""

def inflect(verb, person, number):
    pos = {'are':0, 'ere':1, 'ire':2}
    base = verb[:len(verb)-3]
    end = verb[len(verb)-3:]
    p = pronomi[person][number]
    vs = verbi_spec[person][number][pos[end]]
    vc = verbi_com[person][number]
    return p + ' ' + base + vs + vc

