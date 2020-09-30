import random as r
j=11

def game():
	deck=[2,3,4,5,6,7,8,9,10,j]*4
	score=0

	r.shuffle(deck)
	print("Let's play?")
	
	while True:
	    choice=input('Take a card? y/n\n')
	    if choice=='y':
	        card=deck.pop()
	        print(f'Yours card rang is {card}')
	        score+=card

	        if score>21:
	            print('You lose :(')
	            break
	        elif score==21:
	            print('VICTORY!')
	            break
	        else:
	            print(f'You have {score} points')
	    elif choice=='n':
	        print(f'You have {score} points, and you finish the game.')
	        break

def BotGame():
	CountOfGames=int(input("How much games? "))
	Epoch=int(input("What epochs? "))

	for _ in range(Epoch+1):
		wins=0
		loses=0

		for _ in range(CountOfGames+1):
			deck=[2,3,4,5,6,7,8,9,10,j]*4
			score=0

			r.shuffle(deck)
			
			while True:
				card=deck.pop()
				score+=card

				if score>21:
					loses+=1
					break
				elif score==21:
					wins+=1
					break
		print(f"Wins = {wins}, loses = {loses}, winrate = {round(wins*100/(wins+loses))}%")

if __name__=="__main__":
	while True:
		print("What type of game do you want to play?")
		print("--------------------")
		print("1. Simple")
		print("2. Auto bot")
		print("--------------------\n")
		choice=input("= ")

		if choice=="1":
			game()
			break
		elif choice=="2":
			BotGame()
			break