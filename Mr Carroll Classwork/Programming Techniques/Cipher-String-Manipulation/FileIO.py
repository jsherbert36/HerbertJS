def read_text():
    finish = False
    while finish == False:
        file = input("Please enter the input file name i.e input.txt: ")
        try:
            f = open(file,"rt")
            finish = True
        except FileNotFoundError:
            print('File not found - try again')
    
    return (f.read())
    f.close()
#endprocedure
def output_text(String):
    file = input("Please enter the output file name: ")    
    f = open(file,"wt")        
    f.write(String)
    f.close()
#endprocedure

