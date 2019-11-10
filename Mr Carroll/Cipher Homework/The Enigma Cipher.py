### SRC - This is a great effort. I look forward to seeing the OOP version
from FileIO import read_text,output_text

def Rotor(RotorNum,Character,Direction):   #Rotors are accurate to German WWII specs
	RotorPatterns = [[['A','E'],['B','K'],['C','M'],['D','F'],['E','L'],['F','G'],        #Rotor I 
		            ['G','D'],['H','Q'],['I','V'],['J','Z'],['K','N'],['L','T'],
		            ['M','O'],['N','W'],['O','Y'],['P','H'],['Q','X'],['R','U'],
		            ['S','S'],['T','P'],['U','A'],['V','I'],['W','B'],['X','R'],
		            ['Y','C'],['Z','J']],
                            [['A','A'],['B','J'],['C','D'],['D','K'],['E','S'],['F','I'],       #Rotor II
		            ['G','R'],['H','U'],['I','X'],['J','B'],['K','L'],['L','H'],
		            ['M','W'],['N','T'],['O','M'],['P','C'],['Q','Q'],['R','G'],
		            ['S','Z'],['T','N'],['U','P'],['V','Y'],['W','F'],['X','V'],
		            ['Y','O'],['Z','E']],
                                [['A','B'],['B','D'],['C','F'],['D','H'],['E','J'],['F','L'],         #Rotor III
                                ['G','C'],['H','P'],['I','R'],['J','T'],['K','X'],['L','V'],
			        ['M','Z'],['N','N'],['O','Y'],['P','E'],['Q','I'],['R','W'],
			        ['S','G'],['T','A'],['U','K'],['V','M'],['W','U'],['X','S'],
			        ['Y','Q'],['Z','O']],
                                [['A','E'],['B','S'],['C','O'],['D','V'],['E','P'],['F','Z'],         #Rotor IV
                                ['G','J'],['H','A'],['I','Y'],['J','Q'],['K','U'],['L','I'],
			        ['M','R'],['N','H'],['O','X'],['P','L'],['Q','N'],['R','F'],
			        ['S','T'],['T','G'],['U','K'],['V','D'],['W','C'],['X','M'],
			        ['Y','W'],['Z','B']],
				[['A','V'],['B','Z'],['C','B'],['D','R'],['E','G'],['F','I'],         #Rotor V
                                ['G','T'],['H','Y'],['I','U'],['J','P'],['K','S'],['L','D'],
			        ['M','N'],['N','H'],['O','L'],['P','X'],['Q','A'],['R','W'],
			        ['S','M'],['T','J'],['U','Q'],['V','O'],['W','F'],['X','E'],
			        ['Y','C'],['Z','K']]]

	if Direction == 'Normal':
		for i in range(26):
			if Character == RotorPatterns[RotorNum - 1][i][0]:
				return RotorPatterns[RotorNum - 1][i][1]
			#endif
		#next i
	elif Direction == 'Inverse':
		for i in range(26):
			if Character == RotorPatterns[RotorNum - 1][i][1]:
				return RotorPatterns[RotorNum - 1][i][0]
			#endif
		#next i
	#endif

def IterateRotor(Text,SettingList,RotorChoice,ReflectorChoice):
	#create array with starting positions of rotors
	Position = [0,0,0]
	for i in range(1,3):
		if SettingList[i] == 1:
			Position[i] = 26
		else: 
			Position[i] = SettingList[i] - 1
		#endif
	#next i
	#move through rotors while changing character
	NextRotor = [18,6,23,11,1]												
	Final = []
	Finish = False
	TextCount = 0
	while Finish == False:
		Position[1] += 1
		
		while Position[1] != NextRotor[RotorChoice[1]-1] and Finish == False:
			Position[2] += 1
			
			while Position[2] != NextRotor[RotorChoice[2]-1] and Finish == False:
				
				TextCount += 1
				if TextCount == len(Text):
					Finish = True
				#endif
				
				Shift = Position[2] 				
				Letter1_Shift = ((ord(Text[TextCount - 1]) + Shift - 65) % 26) + 65			#letter must be shifted according to difference in positions of rotors				
				Letter1 = Rotor(RotorChoice[2],chr(Letter1_Shift),'Normal')				#letter then goes through rotor

				Shift = Position[1] - Position[2]
				Letter2_Shift = ((ord(Letter1) + Shift - 65) % 26) + 65
				Letter2 = Rotor(RotorChoice[1],chr(Letter2_Shift),'Normal')
				
				Shift = Position[0] - Position[1]
				Letter3_Shift = ((ord(Letter2) + Shift - 65) % 26) + 65
				Letter3 = Rotor(RotorChoice[0],chr(Letter3_Shift),'Normal')

				Shift = 0 - Position[0]
				Letter4_Shift = ((ord(Letter3) + Shift - 65) % 26) + 65 
				Letter4 = chr(Letter4_Shift)

				ReflectedLetter = reflector(Letter4,ReflectorChoice)					#letter is reflected 

				Shift = Position[0] 
				InvLetter4_Shift = ((ord(ReflectedLetter) + Shift - 65) % 26) + 65			#letter is shifted back
				

				InvLetter3 = Rotor(RotorChoice[0],chr(InvLetter4_Shift),'Inverse')			#letter goes back through rotors
				Shift = Position[1] - Position[0]
				InvLetter3_Shift = ((ord(InvLetter3) + Shift - 65) % 26) + 65
				
				InvLetter2 = Rotor(RotorChoice[1],chr(InvLetter3_Shift),'Inverse')
				Shift = Position[2] - Position[1]
				InvLetter2_Shift = ((ord(InvLetter2) + Shift - 65) % 26) + 65
				
				InvLetter1 = Rotor(RotorChoice[2],chr(InvLetter2_Shift),'Inverse')
				Shift = 0 - Position[2] 				
				InvLetter1_Shift = ((ord(InvLetter1) + Shift - 65) % 26) + 65 			
				

				Final.append(chr(InvLetter1_Shift))
											
				Position[2] = (Position[2] + 1) % 26  #move rotor one step
			#endwhile
			Position[1] = (Position[1] + 1) % 26
		#endwhile	
		Position[0] = (Position[0] + 1) % 26
	#endwhile
	return Final


def reflector(Character,Reflector):
	ReflectorB_C = [[['A','Y'],['B','R'],['C','U'],['D','H'],['E','Q'],['F','S'],                   #Reflector B
			   ['G','L'],['I','P'],['J','X'],['K','N'],['M','O'],['T','Z'],['V','W']],
			[['A','F'],['B','V'],['C','P'],['D','J'],['E','I'],['G','O'],			#Reflector C
			   ['H','Y'],['K','R'],['L','Z'],['M','X'],['N','W'],['T','Q'],['S','U']]]
	if Reflector == 'B':
		num = 0
	elif Reflector == 'C':
		num = 1
	#endif
	for i in range(13):
		if Character == ReflectorB_C[num][i][0]:
			return ReflectorB_C[num][i][1]
		elif Character == ReflectorB_C[num][i][1]:
			return ReflectorB_C[num][i][0]
		#endif
	#next i

def ConfigPlugBoard():
	Letters = []
	Record = []
	print("Enter a pair of letters to swap such as: AB or CD")
	print("You can swap up to ten pairs of letters")
	print("Enter -1 when you have entered all the pairs")
	while len(Letters) < 10:		
		print('Pair ',len(Letters) +1,':',sep ='',end='')
		Pair = input()
		if Pair == "-1":
			break
		elif len(Pair) != 2 or Pair.isnumeric():
			print("Invalid input")
		elif Pair[0] in Record or Pair[1] in Record:
			print("Letters can only be used once")
		else:
			Letters.append([Pair[0],Pair[1]])
			Record.append(Pair[0])
			Record.append(Pair[1])
		#endif
	#endwhile
	return Letters #returns list of letters to swap


def Plugboard(Text,Letters):    #takes a list as input
	for i in range(len(Text)):  #swaps letters
		for j in range(len(Letters)):
			if Text[i] == Letters[j][0]:
				Text[i] = Letters[j][1]
			elif Text[i] == Letters[j][1]:
				Text[i] = Letters[j][0]
			#endif
		#next j
	#next i
	return Text  #returns it as a list

			
def ChooseRotors():
	RotorOrder = []
	print("Choose which three rotors to use in which order:")
	print("You can choose from rotors 1 to 5")
	while len(RotorOrder) < 3:
		print("Position ", len(RotorOrder)+1," - (from left to right): ",sep = '',end = '')
		Rotor = int(input())
		if Rotor in RotorOrder:
			print("Rotors can only be used once")
		elif Rotor > 5 or Rotor == 0:
			print("Invalid input")
		else:
			RotorOrder.append(Rotor)
		#endif
	#endwhile
	return RotorOrder


def InputText():
	UserInput = read_text()
	PlainText = []
	for letter in UserInput:
		if letter.isalpha():
			PlainText.append(letter.upper())
		#endif
	#next letter
	return PlainText #returns a list


def ChoosePosition():
	RotorPosition = []
	print("Choose the numerical rotor positions from 1 - 26:")
	while len(RotorPosition) < 3:
		print("Enter setting for rotor ", len(RotorPosition) + 1,": ",sep='',end='')
		Rotor = input()	
		if Rotor.isalpha():
			print("Invalid input")
		elif int(Rotor) > 26 or int(Rotor) == 0:
			print("Invalid input")
		else:
			RotorPosition.append(int(Rotor) - 1)
		#endif
	#endwhile
	return RotorPosition


def ChooseReflector():
	Finish = False
	while Finish == False:
		Reflector = (input("Enter B or C to choose reflector: ")).upper()
		if Reflector == 'B' or Reflector == 'C':
			return Reflector
			Finish == True
		else:
			print("Invalid input - try again!")
		#endif
	#endwhile

RotorChoice = ChooseRotors()
Positions = ChoosePosition()
PlugLetters = ConfigPlugBoard()
Reflector = ChooseReflector()
print('You have configured the machine')
PlainText = InputText()

CipherText = Plugboard(PlainText,PlugLetters)
CipherText = IterateRotor(PlainText,Positions,RotorChoice,Reflector)
FinalText = Plugboard(CipherText,PlugLetters)
output_text("".join(FinalText))
