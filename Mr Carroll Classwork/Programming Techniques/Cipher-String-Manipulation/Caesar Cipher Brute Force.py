from FileIO import read_text,output_text
def bruteforce(string):
    for key in range(1,27):   
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
        print(key,". ",translated,sep='')
        print('====================================================')
    #nextkey

answer = read_text()     
bruteforce(answer)
