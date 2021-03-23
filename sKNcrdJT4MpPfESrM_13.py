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
    disk = files.replace('PC Files: ', '').split(', ')
    clean_files = []
​
    for i, f in enumerate(disk):
        if 'virus' in f:
            search = f.split('virus')
            if search[0] in ['not', 'anti']:
                clean_files.append(f)
        elif 'malware' not in f:
            clean_files.append(f)
​
    if not clean_files:
        return 'PC Files: Empty'
    return 'PC Files: ' + ', '.join(clean_files)

