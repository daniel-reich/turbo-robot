"""
Each person in Italy has an unique identifying ID code issued by the national
tax office after the birth registration: the Fiscal Code ( _Codice Fiscale_ ).
Check the **Resources** tab for more info on this.

Given a dictionary containing the personal data of a person (name, surname,
gender and date of birth) return the 11 code characters as a string following
these steps:

  * Generate 3 capital letters from the **surname** , if it has:

    * At least 3 consonants then the first three consonants are used. ( _Newman - > NWM_).
    * Less than 3 consonants then vowels will replace missing characters in the same order they appear ( _Fox - > FXO | Hope -> HPO_).
    * Less than three letters then "X" will take the third slot after the consonant and the vowel ( _Yu - > YUX_).
  * Generate 3 capital letters from the **name** , if it has:

    * Exactly 3 consonants then consonants are used in the order they appear ( _Matt - > MTT_).
    * More than 3 consonants then first, third and fourth consonant are used ( _Samantha - > SNT | Thomas -> TMS_).
    * Less than 3 consonants then vowels will replace missing characters in the same order they appear ( _Bob - > BBO | Paula -> PLA_).
    * Less than three letters then "X" will take the the third slot after the consonant and the vowel ( _Al - > LAX_).
  * Generate 2 numbers, 1 letter and 2 numbers from **date of birth** and **gender** :

    * Take the last two digits of the year of birth ( _1985 - > 85_).
    * Generate a letter corresponding to the month of birth ( _January - > A | December -> T_) using the table for conversion included in the code.
    * For males take the day of birth adding one zero at the start if is less than 10 ( _any 9th day - > 09 | any 20th day -> 20_).
    * For females take the day of birth and sum 40 to it ( _any 9th day - > 49 | any 20th day -> 60_).

### Examples

    fiscal_code({
      "name": "Matt",
      "surname": "Edabit",
      "gender": "M",
      "dob": "1/1/1900"
    }) ➞ "DBTMTT00A01"
    
    fiscal_code({ 
      "name": "Helen",
      "surname": "Yu",
      "gender": "F",
      "dob": "1/12/1950"
    }) ➞ "YUXHLN50T41"
    
    fiscal_code({
      "name": "Mickey",
      "surname": "Mouse",
      "gender": "M",
      "dob": "16/1/1928"
    }) ➞ "MSOMKY28A16"

### Notes

  * Code letters must be uppercase.
  * Date of birth is given in D/M/YYYY format.
  * The conversion table for months is already in the starting code.
  * Y is not a vowel.

"""

months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
    
    
    n=person["name"].lower()
    s=person["surname"].lower()
    g=person["gender"]
    d=person["dob"].split("/")
    
    nn, ss, gg, mscn,mscs = [], [], [], [], []
    cnst="zrtypqsdfghjklmwxcvbn"
​
    
    for i in n:
        if i in cnst:
            nn.append(i)
        else:
            mscn.append(i)   
    if len(nn)>3:
        fnn = (nn[0]+nn[2]+nn[3]).upper()
    elif len(nn)==3:
        fnn = (nn[0]+nn[1]+nn[2]).upper()
    elif len(nn)<2:
        fnn = (nn[0]+mscn[0]+"X").upper()        
    elif len(nn)<3:
        fnn = (nn[0]+nn[1]+mscn[0]).upper()        
    for i in s:
        if i in cnst:
            ss.append(i)
        else:
            mscs.append(i)
    if len(ss)>3:
        fss = (ss[0]+ss[2]+ss[3]).upper()
    elif len(ss)==3:
        fss = (ss[0]+ss[1]+ss[2]).upper()
    elif len(ss)<2:
        fss = (ss[0]+mscs[0]+"X").upper()                
    elif len(ss)<3:
        fss = (ss[0]+ss[1]+ mscs[0]).upper()        
    
    fdy = d[2][-2:]
    fdm = months[d[1]]
    
    if g == "F":
        fdd = str(40+int(d[0]))
    if g == "M":
        if int(d[0]) < 10:
            fdd = "0"+d[0]
        else:
            fdd = d[0]
        
​
    
    return (fss+fnn+fdy+fdm+fdd)

