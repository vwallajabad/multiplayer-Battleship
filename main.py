import replit
#Board

hello = True
guessnumber = 0
shipsdown = 0
print("1 2 3 4 5 6 7 8 9 10")
board = [
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
    "*",
]
print(board[0], board[1], board[2], board[3], board[4], board[5], board[6],
      board[7], board[8], board[9] + "a")
print(board[10], board[11], board[12], board[13], board[14], board[15],
      board[16], board[17], board[18], board[19] + "b")
print(board[20], board[21], board[22], board[23], board[24], board[25],
      board[26], board[27], board[28], board[29] + "c")
print(board[30], board[31], board[32], board[33], board[34], board[35],
      board[36], board[37], board[38], board[39] + "d")
print(board[40], board[41], board[42], board[43], board[44], board[45],
      board[46], board[47], board[48], board[49] + "e")
print(board[50], board[51], board[52], board[53], board[54], board[55],
      board[56], board[57], board[58], board[59] + "f")
print(board[60], board[61], board[62], board[63], board[64], board[65],
      board[66], board[67], board[68], board[69] + "g")
print(board[70], board[71], board[72], board[73], board[74], board[75],
      board[76], board[77], board[78], board[79] + "h")
print(board[80], board[81], board[82], board[83], board[84], board[85],
      board[86], board[87], board[88], board[89] + "i")
print(board[90], board[91], board[92], board[93], board[94], board[95],
      board[96], board[97], board[98], board[99] + "j")
print("Enter values like a1 c4")
#Set ship values
Ship1 = input("Ship 1: ")
Ship2 = input("Ship 2: ")
Ship3 = input("Ship 3: ")
Ship4 = input("Ship 4: ")
Ship5 = input("Ship 5: ")
Ship6 = input("Ship 6: ")
Ship7 = input("Ship 7: ")
Ship8 = input("Ship 8: ")
Ship9 = input("Ship 9: ")
Ship10 = input("Ship 10: ")
replit.clear()
print("1 2 3 4 5 6 7 8 9 10")
print(board[0], board[1], board[2], board[3], board[4], board[5], board[6],
      board[7], board[8], board[9] + "a")
print(board[10], board[11], board[12], board[13], board[14], board[15],
      board[16], board[17], board[18], board[19] + "b")
print(board[20], board[21], board[22], board[23], board[24], board[25],
      board[26], board[27], board[28], board[29] + "c")
print(board[30], board[31], board[32], board[33], board[34], board[35],
      board[36], board[37], board[38], board[39] + "d")
print(board[40], board[41], board[42], board[43], board[44], board[45],
      board[46], board[47], board[48], board[49] + "e")
print(board[50], board[51], board[52], board[53], board[54], board[55],
      board[56], board[57], board[58], board[59] + "f")
print(board[60], board[61], board[62], board[63], board[64], board[65],
      board[66], board[67], board[68], board[69] + "g")
print(board[70], board[71], board[72], board[73], board[74], board[75],
      board[76], board[77], board[78], board[79] + "h")
print(board[80], board[81], board[82], board[83], board[84], board[85],
      board[86], board[87], board[88], board[89] + "i")
print(board[90], board[91], board[92], board[93], board[94], board[95],
      board[96], board[97], board[98], board[99] + "j")
print("Pass to player two")
print("Enter values like a1 c4")
print("type giveup to give up")
while hello:
	Guess = input("Type your guess: ")

	if Guess == Ship1:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	if Guess == Ship2:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	if Guess == Ship3:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	if Guess == Ship4:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	if Guess == Ship5:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	if Guess == Ship6:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	if Guess == Ship7:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	if Guess == Ship8:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	if Guess == Ship9:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	if Guess == Ship10:
		print("Good job!! You took down one ship!")
		shipsdown += 1

	guessnumber += 1
	if shipsdown == 10:
		print("Your score is: ")
		print(guessnumber)
		break
		
	if Guess == "giveup":
	  print(Ship1)
	  print(Ship2)
	  print(Ship3)
	  print(Ship4)
	  print(Ship5)
	  print(Ship6)
	  print(Ship7)
	  print(Ship8)
	  print(Ship9)
	  print(Ship10)
	  break
