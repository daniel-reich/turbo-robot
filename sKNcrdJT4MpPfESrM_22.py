"""


Your computer might have been infected by a virus! Create a function that
finds the viruses in `files` and removes them from your computer.

### Examples

    remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg") ➞ "PC Files: spotifysetup.exe, dog.jpg"
    
    remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ") ➞ "PC Files: antivirus.exe, cat.pdf"
    
    remove_virus("PC Files: notvirus.exe, funnycat.gif") ➞ "PC Files: notvirus.exe, funnycat.gif")

### Notes

  * Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
  * Return `"PC Files: Empty"` if there are no files left on the computer.

"""

def remove_virus(files):
    temp = files[10:].split(', ')
    myans = []
    for i in temp:
        if 'virus' in i:
            if i == 'notvirus.exe':
                myans.append(i)
            if i == 'antivirus.exe':
                myans.append(i)
​
        elif 'malware' in i:
            pass
​
        else:
            myans.append(i)
​
    if len(myans) == 0:
        return 'PC Files: Empty'
    else:
        return 'PC Files: ' + ', '.join(myans)

