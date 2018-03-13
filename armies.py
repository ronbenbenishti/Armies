import urllib.request as ur

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
    print("%s file has been created" % (file))
    # linksmaker(305)     # start from 0 up to 305.

# Update MD5 datebase
def Update():
    print("#"*21 + "\n# UPDATE LINKS FILE #\n" + "#"*21)
    updatechoose = input("update links file? (y/n): ")
    if updatechoose == "y":
        howmany = int(input("Choose how many links to create? (306 links available)"))
        if howmany > 0 and howmany < 307:
            Linksmaker(howmany-1)
        else:
            print("invalid input")
    elif updatechoose == "n":
        f = open("lists.txt","r")
        readlistsfile = f.read()
        f.close()
        readlines = readlistsfile.split("\n")
        readlines.remove("")

        file = "db.txt"
        f = open(file, "w")     # cleaning db file
        f.close()               # -------||-------
        f = open(file, "a")
        num = 1
        for link in readlines:
            print("opening url num " + str(num))
            urlopen = ur.urlopen(link)
            print("reading url..")
            db = str(urlopen.read())
            dblist = db.split("\\n")
            print("writing to %s" % (file))
            del dblist[0:6]
            for x in dblist:
                f.write(x + "\n")
            num += 1
        f.close()
        print("Completed.\n")
    else:
        print("Invalid input")
    anykey = input("press any key to continue..")

# Generate MD5
def MD5(file):
    import hashlib
    hash_md5 = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Compare MD5 to databate
def Scan(filetoscan):
    fname="db.txt"
    file = open(fname,'r')
    md5table = file.readlines()
    file.close()
    try:
        md5code = MD5(filetoscan)
        print("File name: %s\nMD5: %s\n" % (filetoscan, md5code))
        if md5code+'\n' in md5table:
            print("MD5 match has been found!\nFile is infected\n")
        else:
            print("No MD5 match results!\nFile is OK\n")
    except:
        print("File not found..")
    a=input("press any key to continue..")


# MENU
while True:
    choose=""
    print("")
    print("#"*30)
    print("# Welcome to Armies          #")
    print("# *****************          #")
    print("#                            #")
    print("# 1) Update database         #")
    print("# 2) Scan file               #")
    print("# 3) Scan full path          #")
    print("#                            #")
    print("# press 'q' to quit          #")
    print("#"*30)
    choose = input("Select your choice: ")
    if choose == "1":
        Update()
    elif choose == "2":
        Scan(input("Enter file name: "))
    elif choose == "3":
        pass
    elif choose == "q":
        quit()
    else:
        print("Invalid input")
