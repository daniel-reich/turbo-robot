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
    lst = files[files.index(":")+1::].split(", ")
    result = list()
    for file in lst:
        if "virus" in file and "antivirus" not in file and "notvirus" not in file:
            pass
        elif "malware" in file:
            pass
        else:
            result.append(file)
    return "PC Files:"+", ".join(result) if result else "PC Files: Empty"

