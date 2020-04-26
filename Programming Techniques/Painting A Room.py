unit = 'x'
while unit == 'x':
    print('Enter imperial or metric')
    value = input()
    if value == 'metric':
        unit = 'metres'
    elif value == 'imperial':
        unit = 'feet'
    else:
        print('invalid input')
print('Enter the height, width and length of the room - in that order, in ',unit,'.')
height = float(input())
width = float(input())
length = float(input())
SA =((height*width*2) + (height*length*2) + (width * length)) 
print('You need enough paint to cover ',SA,' ', unit, ' squared.')


