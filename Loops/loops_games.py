import random

money = 100

		
def generator(num, bet):
	global money
	num = random.randint(1, 10)
	return num
	if num >= bet:
		money = money * 2
		print ("Win!")
	else:
		money = money - (money/2)
		print ("Lose!")
	
generator(num, 8)


import random

money = 100

#Write your game of chance functions here
def flip_coin(bet, x):
  num = random.randint(1, 2)
  if (num == x):
    print("Win!" + " " + str(bet))
  else: 
	  print("Lose!" + " " + str (-bet))
    
flip_coin(20, 1)


def cho_han(bet, s):
  num = random.randint(2, 12)
  if num%2 == 0 and s%2 == 0:
    print("Win!", "Even", str(bet))
  elif num%2 == 1 and s%2 == 1:
    print("Win!", "Odd", str(bet))
  elif num%2 == 0 and s%2 == 1:
    print("Lose!", "Even", str(-bet))
  elif num%2 == 1 and s%2 == 0:
    print("Lose!", "Odd", str(-bet))

cho_han(10, 8)


def deck_cards(bet):
  num1 = random.randint(1, 9)
  num2 = random.randint(1, 9)
  if num1 > num2:
    print(num1, num2, str(bet))
  elif num1 == num2:
    return 0
  else:
    print(num2, num1, str(-bet))
  
deck_cards(30)
  
	
	