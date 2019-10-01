def read_text():
    file = input("Please enter the input file name i.e input.txt: ")
    f = open(file,"rt")
    return (f.read()).upper()
    f.close()
#endprocedure
def output_text(String):
    file = input("Please enter the output file name: ")
    f = open(file,"wt")
    f.write(String)
    f.close()
#endprocedure

