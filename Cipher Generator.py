def cipherText(string, key):                            #Function cipherText, with arguments 'string' and 'key'. Encrypts text.
    cipher_text = []                                    #initializes 'cipher_text' as a list.
    print("Encrypting...")                              #prints "Encrypting..." to show encryption is in progress.
    for i in range(len(string)):                        #for loop, iterates over length of string, 'i' is current int in iteration.
        x = (ord(string[i]) + ord(key[i])) % 26         #the int 'x' is set to the value of the unicode of the (i)nth int in 'string' to (i)nth int in 'key', which is then divided by 26.
        x += ord('A')                                   #the int 'x' has the unicode value of A(65) added to it.
        cipher_text.append(chr(x))                      #the value of 'x' is appended to the 'cipher_text' list.
    print("Done")                                       #"Done" is printed to show that the encryption has finished.
    return ("" . join(cipher_text))                     #the list 'cipher_text' is turned into a string with no spaces inbetween the letters, and returned as the value of cipherText.

def originalText(cipher_text, key):                     #function originalText, with arguments cipher_text and key. Decrypts text.
    orig_text = []                                      #initializes orig_text as a list.
    print("Decrypting...")                              #prints "Decrypting..." to show decryption in progress.
    for i in range(len(cipher_text)):                   #for loop, iterates over length of cipher_text(string), 'i' is current int in iteration.
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26 #the int x is set to the value of the unicode of the (i)nth int in cipher_text to (i)nth int in key, the value has 26 added to it then 26 divided from it.
        x += ord('A')                                   #the int x has the unicode value of A(65) added to it.
        orig_text.append(chr(x))                        #the value of x is appended to list orig_text.
    print("Done")                                       #"Done" is printed to show that the Decryption has finished.
    return("" . join(orig_text))                        #the list orig_text is turned into a string with no spaces inbetween the letters, and then returned as the value of originalText.

def generateKey(string, kraw):                          #Function generateKey, with arguments string and kraw. creates a key matching length of 'string'.
    key = list(kraw)                                    #the int 'kraw' is turned into a list, which is then transferred to 'key'.
    if len(string) == len(key):                         #If the length of 'string' is equal to the length of 'key',
        return(key)                                     #the value of 'key' is returned as value of generateKey.
    else:                                               #Else,
        for i in range(len(string) - len(key)):         #for loop, total length of 'string'(length) minus 'key'(length), is iterated over by 'i'.
            key.append(key[i % len(key)])               #the value of the key divided by the iteration 'i' is appended to 'key' list, creating a list that should look like keykeykeyke...etc that matches the length of the 'string'.
    return("" . join(key))                              #the list 'key' is srtipped of spaces and converted into a string, then returned as value of generateKey.
    

selection = int(input("What would you like to do today?\n 1 for creating a key\n 2 for encrypting an HTML file\n 3 for Decrypting an HTML file\n")) ##'selection' int is obtained by asking the user a question regarding what they would like to program to do.

def kquery():                                           #function kquery. Obtains key from .txt file or creates one.
    have = str(input("Do you have a key or do you need to make one? h/m\n")) #prompts user if they (h)ave a key, or need to (m)ake one. Value is stored in 'have'.
    if have == str("h"):                                    #If user (h)as a key,
         keypath = input("Enter filepath for key location (.txt file): ") #asks location for the .txt file containing the key, stores value in keypath.
         with open(keypath,"r") as file:                #opens the file indicated by 'keypath' as read only.
            k = file.read().rstrip()                    # the file is read and rstrip() removes spaces at end and beginning, string is stored in 'k'.
         klist = list(k)                                #string 'k' is converted into list(), stored in 'klist'
         return klist                                   #'klist' is returned as value fof kquery()
    else:                                                   #Else,
        import random                                   #imports Random.
        keylong = int(input("Enter Key Length Integer: ")) #gets integer of how long key should be.
        keything = ''                                   #initializing key storage.
        keychain = ''                                   #initializing keychain storage.
        asciicode = list(map(chr, range(32, 126)))      #creates List 'asciicode' using Ascii digits.
        keychain = (random.choices(asciicode, k=keylong)) #randomly selects digits from 'asciicode', 'keylong' amount of times, stores in List 'keychain'.
        keything = ''.join(map(str,keychain))           #turns List 'keychain' into a string "keything".
        print("Your Key is ==>"+keything+"<== Please create a text doc and store the key inside.") #shows user the randomly generated key.
        return keything                                 #returns 'keything' as value for kquery().
        
def fileenc():                                          #Function fileenc(). finds location of file to be encrypted. 
    import codecs                                       #import codecs to allow for direct manipulation of html files.
    userpath = input("Enter filepath for HTML file you would like to encrypt: ") #gets location of file to be encrypted from user, stores in 'userpath'.
    with codecs.open(userpath,"r") as file:             #opens the file indicated by 'userpath' as read only.
        fstring = file.read().rstrip()                  #the file is read and stripped of leading and trailing spaces. file contents copied in 'fstring'
    flist = list(fstring)                               #'fstring' converted into list 'flist'
    return flist                                        #'flist' returned as value of fileenc().

def fileDec():                                          #Function fileDec(). finds location if file to be decrypted.
    import codecs                                       #import codecs to allow for direct manipulation of html files.
    userpath = input("Enter filepath for HTML file you would like to decrypt: ") #gets location of file to be decrypted from user, stored in 'userpath'
    with codecs.open(userpath, "r") as file:            #opens the file indicated by 'userpath' as read only.
        fstring = file.read().rstrip()                  #the file is read and stripped of leading and trailing spaces. file contents copied to 'fstring'.
    flist = list(fstring)                               #'fstring' converted to list 'flist'
    return flist                                        #'flist' returned as value of fileDec().

if (selection == 1):                                    ##if earlier the user entered 1,
    key = kquery()                                      ##function kquery() would be called, and user would recieve a random key

elif (selection == 2):                                  ##if earlier the user selected 2,
    kraw = kquery()                                     ##function kquery() would be called to get the user's key. key would be stored in 'kraw'.
    string = fileenc()                                  ##function fileenc() would be called to get the contents of the file the user wants to encrypt, and stores them in 'string'.
    key = generateKey(string,kraw)                      ##function generateKey(string,kraw) would be called to turn the user's key into a string matching the length of the text in the file.
    filename = input("What should the name of the new file be? (Do not add file extension ending, .htm, .html, etc.") ##asks user for what they would like the new name of the file to be. stores value in 'filename'
    creahtm = filename + '_enc'                         ##appends "_enc" to the end of the file, stores in 'creahtm'.
    end = creahtm + '.html'                             ##turns the .txt into a .html file, stores in 'end'.                
    with open(end, 'w') as file:                        ##Creates new file using the name in 'end'.
        file.write(cipherText(string, key))             ##function cipherText(string,key) is called, writes resulting text to the opened file.
    
elif (selection ==3):                                   ##if earlier the user entered 3,
    kraw = kquery()                                     ##function kquery() would be called to get the user's key. key would be stored in 'kraw'.
    string = fileDec()                                  ##function fileDec() would be called to get the contents of the file the user wants to decrypt, and stores them in 'string'.
    key = generateKey(string,kraw)                      ##function generateKey(string,kraw) would be called to turn the user's key into a string matching the length of the text in the file.
    cipher_text = string                                ##text from fileDec() would be copied over to cipher_text.
    filename = input("What should the name of the new file be? (Do not add file extension ending, .htm, .html, etc") ##asks user for what they would like the new name of the file to be. stores value in 'filename'
    creahtm = filename + '_dec'                         ##appends "_dec" to end of file.
    end = creahtm + '.html'                             ##turns the .txt into a .html file, stores in 'end'.
    with open (end, 'w') as file:                       ##creates new file using the name in 'end'
        file.write(originalText(cipher_text, key))      ##function originalText(cipher_text, key) is called, writes resulting text to the opened file.
    
