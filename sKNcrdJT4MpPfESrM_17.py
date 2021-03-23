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

def remove_virus(lst):
    lst = lst[10:]
    lst = lst.split(", ")
    newlst = []
    for i in lst:
        var = i.split(".")
        vartest = var[0]
        if "virus" in vartest or "malware" in vartest:
            if "antivirus" in vartest or "notvirus" in vartest:
                newlst.append(var[0] + "." + var[1])
        else:
            newlst.append(i)
    if len(newlst) != 0:
        lstresult = "PC Files:"
        for i in newlst:
            lstresult = lstresult + " " + i + ","
        lstresult = lstresult[:-1]
    else:
        lstresult = "PC Files: Empty"
    return lstresult;

