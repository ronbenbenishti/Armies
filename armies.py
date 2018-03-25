import urllib.request as ur

Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Default = '\033[99m'
Bold = '\033[1m'

# Create links file
def Linksmaker(filesQty):
    file = "lists.txt"
    link = "https://virusshare.com/hashes/VirusShare_00"
    ext = ".md5"
    f = open(file,"w")
    for x in range(0,filesQty+1):
        if x < 10:
            f.write(link + "00" + str(x) + ext + "\n")
        elif x < 100:
            f.write(link + "0" + str(x) + ext + "\n")
        else:
            f.write(link + str(x) + ext + "\n")
    print(Green+"%s file has been updated" % (file))
    # linksmaker(305)     # start from 0 up to 305.

# Update MD5 datebase
def Update():
    f = open("lists.txt","r")
    readlistsfile = f.read()
    f.close()
    readlines = readlistsfile.split("\n")
    readlines.remove("")

    file = "db.txt"
    f = open(file, "w")
    num = 1
    for link in readlines:
        print(Green+"Opening URL "+Blue+"#"+str(num)+Default)
        urlopen = ur.urlopen(link)
        print(Green+"Reading URL "+Blue+"#"+str(num)+Default)
        db = str(urlopen.read())
        dblist = db.split("\\n")
        print(Green+"Writing to "+Blue+file+Default)
        del dblist[0:6]
        for x in dblist:
            f.write(x + "\n")
        num += 1
    f.close()
    f = open(file, "r")
    HowMuchMD5 = len(f.readlines())
    print(Green+"MD5 Quantity: "+Blue+str(HowMuchMD5))
    print(Green+"Completed.\n"+Default)

# Generate MD5
def MD5(file):
    import hashlib
    hash_md5 = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Compare MD5 to databate
def SingleScan(filetoscan):
    fname="db.txt"
    file = open(fname,'r')
    md5table = file.readlines()
    file.close()
    try:
        md5code = MD5(filetoscan)
        print(Default+"-"*34+Green+"\nFile: "+Blue+filetoscan+Green+"\nMD5: "+Blue+md5code)
        if md5code+'\n' in md5table:
            print(Red+"MD5 MATCH HAS BEEN FOUND! - (FILE IS INFECTED!!!)\n"+Default+"-"*34)
        else:
            print(Green+"No MD5 match results! - (File is OK)\n"+Default+"-"*34)

    except:
        print(Red+"Error: File not selected.."+Default)

oklist=[]
badlist=[]
def Scan(filetoscan):
    fname="db.txt"
    file = open(fname,'r')
    md5table = file.readlines()
    file.close()
    try:
        md5code = MD5(filetoscan)
        print(Default+"%s | MD5: %s" % (filetoscan, md5code))
        if md5code+'\n' in md5table:
            print(Red+"MD5 match has been found! - FILE IS INFECTED!!!"+Default)
            badlist.append(filetoscan)
        else:
            oklist.append("Ok")
    except:
        print(Red+"Error: File not found.."+Default)


def Scanpath(pathToFolder, keyWord):
    print(Green+"Starting to scan..\nPath: "+Blue+pathToFolder+Default)
    import os
    _pathToFiles = []
    _fileNames = []

    for dirPath, dirNames, fileNames in os.walk(pathToFolder):
        selectedPath = [os.path.join(dirPath,item) for item in fileNames if item.startswith(keyWord)]
        _pathToFiles.extend(selectedPath)

        selectedFile = [item for item in fileNames if item.startswith(keyWord)]
        _fileNames.extend(selectedPath)

        try:
            _pathToFiles.remove("")
            _imageFiles.remove("")
        except ValueError:
            pass

    oklist.clear()
    badlist.clear()
    for fullpath in _fileNames:
        Scan(fullpath)
    scanned=len(_fileNames)
    ok=len(oklist)
    bad=len(badlist)
    if scanned > 0:
        print("\n"+Blue+str(scanned)+Default+" files were found is searched folder(s)\n"+Blue+str(ok)+Default+" file(s) is OK and "+Blue+str(bad)+Default+" is Infected")
        if bad > 0:
            print(Red+Bold+"*** WARNING! %s infected file(s) has been found on your PC" % (bad)+Default)
            print(Red+ "Infected file(s):")
            for badfile in badlist:
                print(badfile)
        else:
            print(Green+"Everything is OK, No infected file(s) was found."+Default)
    else:
        print(Red+"Error: Path is missing"+Default)
    return _pathToFiles, _fileNames



# MENU              # (While menu has been disabled due to the GUI update)
# while True:
#     choose=""
#     print("")
#     print("#"*30)
#     print("# Welcome to Armies          #")
#     print("# *****************          #")
#     print("#                            #")
#     print("# 1) Update links file       #")
#     print("# 2) Update database         #")
#     print("# 3) Scan file               #")
#     print("# 4) Scan path               #")
#     print("#                            #")
#     print("# press 'q' to quit          #")
#     print("#"*30)
#     choose = input("Select your choice: ")
#     if choose == "1":
#         howmany = int(input("Choose how many links to create? (306 links available)"))
#         if howmany > 0 and howmany < 307:
#             Linksmaker(howmany-1)
#         else:
#             print("invalid input")
#
#     elif choose == "2":
#         Update()
#     elif choose == "3":
#         Scan(input("Enter file name: "))
#     elif choose == "q":
#         quit()
#     else:
#         print("Invalid input")
