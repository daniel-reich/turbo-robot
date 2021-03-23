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

from re import split
def remove_virus(files):
  files=split('[,:]',files)[1:]
  new=[]
  for file in files:
    if 'virus' not in file and 'malware' not in file:
      new.append(file)
    else:
      if 'antivirus'in file or 'notvirus' in file:
        new.append(file)
  if not len(new):
    return 'PC Files: Empty'
  return "PC Files:"+','.join(new)

