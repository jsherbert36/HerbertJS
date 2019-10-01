from FileIO import read_text,output_text
def Caesar_Encrypt(string,key):
    translated = ''
    for symbol in string:
        if symbol.isalpha():
            num = ord(symbol) + key                         
            if symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
                #endif
            elif symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
                #endif
            #endif
            translated += chr(num)
        else:
            translated += symbol
        #endif
    #next symbol
    return(translated)

shift = int(input("Please enter the number to shift characters by: "))
Output = Caesar_Encrypt(read_text(),shift)
output_text(Output)
