import os

os.system('clear')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~RCRACK~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

f = input("~~~~~~~~~~~~(What do you want to do?)~~~~~~~~~~~~~\n  \n1)BRUTEFORCE ZIP FILE [1]\n2)BRUTEFORCE RAR FILE [2]\n   \nYour choice=>")

if f=="1":
    import zipfile
    from tqdm import tqdm
    
    os.system('clear')
    print("~~~~~~~~~~~~~~~~~~~~~RCRACK~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~MAKE SURE THAT THE ZIP AND THE WORDLIST FILE~~~\n~~~~~~~~~~ARE PRESENT IN THIS DIRECTORY~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    zip_file = input("Enter the name of the zip file\n=>")
    wordlist = input("Enter the name of the wordlist file\n=>")
    
    zip_file = zipfile.ZipFile(zip_file)
    n_words = len(list(open(wordlist, "rb")))
    print("Total passwords to test\n=>",n_words)
    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=n_words, unit="word"):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print("PASSWORD FOUND SUCCESSFULLY=>", word.decode().strip())
                exit(0)
    print("!!!!!!!!!!!!!!!!{PASSWORD NOT FOUND}!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!{TRY OTHER WORDLISTS}!!!!!!!!!!!!!!")
if f=="2":
    import rarfile
    from tqdm import tqdm
    
    os.system('clear')
    print("~~~~~~~~~~~~~~~~~~~~~RCRACK~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~MAKE SURE THAT THE RAR AND THE WORDLIST FILE~~~\n~~~~~~~~~~ARE PRESENT IN THIS DIRECTORY~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    rar_file = input("Enter the name of the rar file\n=>")
    wordlist = input("Enter the name of the wordlist file\n=>")
    
    rar_file = rarfile.RarFile(rar_file)
    n_words = len(list(open(wordlist, "rb")))
    print("Total passwords to test\n=>",n_words)
    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=n_words, unit="word"):
            try:
                rar_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print("PASSWORD FOUND SUCCESSFULLY=>", word.decode().strip())
                exit(0)
    print("!!!!!!!!!!!!!!!!{PASSWORD NOT FOUND}!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!{TRY OTHER WORDLISTS}!!!!!!!!!!!!!!")

else:
    print("PLEASE SELECT A VALID OPTION!!")






