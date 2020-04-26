from FileIO import output_text,read_text
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)])
        #next i
    #end if 
    return("" . join(key)) 
#end function     

def originalText(cipher_text, key): 
    orig = [] 
    for i in range(len(cipher_text)): 
        if cipher_text[i].isalpha():
            x = ((ord(cipher_text[i])- ord(key[i]))%26)+ ord('A')         
            orig.append(chr(x))
        else: 
            orig.append(cipher_text[i])
        #endif
    #next i
    return("" . join(orig)) 
#end function   

string = (read_text()).upper()
keyword = (input("Enter the key: ")).upper()
key = generateKey(string, keyword) 
output_text(originalText(string, key)) 
