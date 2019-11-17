import json
def read_text(name = ''):
    finish = False
    while finish == False:
        if name == '':
            file = input("Please enter the input file name i.e input.txt: ")
        else:
            file = str(name)
        try:
            f = open(file,"rt")
            finish = True
        except FileNotFoundError:
            print('File not found - try again')
            name = ''
    return (f.read())
    f.close()
#endprocedure
    s
def output_text(String,name = ''):
    if name == '':
        file = input("Please enter the output file name: ")
    else:
        file = name 
    f = open(file,"wt")        
    f.write(String)
    f.close()
#endprocedure
    
def input_list(name = ''):
    finish = False
    while finish == False:
        if name == '':
            file = input("Please enter the input file name i.e input.json: ")
        else:
            file = str(name)
        try:
            f = open(file,"rt")
            finish = True
        except FileNotFoundError:
            print('File not found - try again')
            name = ''
    return (json.load(f))
    f.close()
#endprocedure

def output_list(List):
    file = input("Please enter the .json output file name: ")    
    f = open(file,"wt")        
    json.dump(List, f)
    f.close()
#endprocedure
