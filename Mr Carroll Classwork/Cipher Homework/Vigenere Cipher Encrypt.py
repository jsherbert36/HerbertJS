### SRC - Excellent, I really like the implementation

from FileIO import read_text,output_text
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)])
        #next i
    #endif
    return("" . join(key)) 
#endfunction      

def cipherText(string, key): 
    cipher = [] 
    for i in range(len(string)): 
        if string[i].isalpha():
            x = ((ord(string[i]) + ord(key[i])) % 26)+ ord('A')
            cipher.append(chr(x))
        else:
            cipher.append(string[i])
        #endif
    #next i
    return("" . join(cipher)) 
#endfunction

Plaintext = (read_text()).upper()   
Keyword = (input("Enter your keyword: ")).upper()
output_text(cipherText(Plaintext,generateKey(Plaintext,Keyword)))
