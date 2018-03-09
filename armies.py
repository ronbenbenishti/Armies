import urllib.request as ur
# Create links file
def linksmaker(filesQty):
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

#Update MD5 datebase
def update():
    print("#"*21 + "\n# UPDATE LINKS FILE #\n" + "#"*21)
    updatechoose = input("update links file? (y/n): ")
    if updatechoose == "y":
        howmany = int(input("Choose how many links to create? (306 links available)"))
        if howmany > 0 and howmany < 307:
            linksmaker(howmany-1)
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
        print("Complated.\n")
    else:
        print("Invalid input")

#MENU
choose = 0
while choose != "q":
    print("")
    print("#"*30)
    print("# Welcome to Armies          #")
    print("# *****************          #")
    print("#                            #")
    print("# 1) Update database         #")
    print("# 2) Scan file               #")
    print("#                            #")
    print("# press 'q' to quit          #")
    print("#"*30)
    choose = input("Select your choice: ")
    if choose == "1":
        update()
    elif choose == "2":
        pass
    elif choose == "3":
        pass
    elif choose == "q":
        quit()
    else:
        print("Invalid input")
