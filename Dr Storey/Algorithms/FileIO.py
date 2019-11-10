import json
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
def input_list():
    finish = False
    while finish == False:
        file = input("Please enter the input file name i.e input.json: ")
        try:
            f = open(file,"rt")
            finish = True
        except FileNotFoundError:
            print('File not found - try again')
    return (json.load(f))
    f.close()

def output_list(List):
    file = input("Please enter the .json output file name: ")    
    f = open(file,"wt")        
    json.dump(List, f)
    f.close()
#endprocedure