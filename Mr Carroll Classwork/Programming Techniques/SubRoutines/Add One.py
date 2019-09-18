num,name = 3,"Dave"
name_list = [name[int(i)] for i in range(len(name))]

def add_one(number):
    return number + 1
#end function

def add_s(name):
    return name + "s"
#end function

def append_s(name):
    name.append("s")
    print (name)
#end procedure

print(add_one(num))
print(num, "\n")

print(add_s(name))
print(name, "\n")

append_s(name_list)
print(name_list)
