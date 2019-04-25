import cardBasics
import random

class BlackJack:

	def __init__(self):
		self.PL_hand_vis = []
		self.PL_hand_val = []
		self.AI_hand_vis = []
		self.AI_hand_val = []
		self.win = 0
		self.deckFunc = cardBasics.Deck(False)
		self.deckFunc.shuffle()
		self.turns = 0

		self.initialTurn()
		while self.win == 0:
			print 'Your Hand:',self.PL_hand_vis
			self.newTurn()

		print self.win,'Wins!'

	def initialTurn(self):
		try:
			for deal in range(4):
				newcard = self.deckFunc.deck.pop()
				if deal % 2 == 0:
					self.PL_hand_vis.append(newcard)
					if newcard.split()[0] in 'JackQueenKing':
						self.PL_hand_val.append(10)
					if newcard.split()[0] == 'Ace':
						self.PL_hand_val.append(input('You drew an Ace. Would you like it to be worth 1 or 11? '))
				else:
					self.AI_hand_vis.append(self.deckFunc.deck.pop())
					self.AI_hand_val.append(int(self.AI_hand_vis[-1].split()[0]))
		except: 
			print 'error'
		self.winCheck()

	def newTurn(self):
		self.playerChoice()
		self.winCheck()
		self.AIChoice()
		self.winCheck()

	def winCheck(self):
		if   sum(self.PL_hand_val) == 21:
			self.win = 'Player'
		elif sum(self.PL_hand_val) > 21:
			self.win = 'AI'
		elif sum(self.AI_hand_val) == 21:
			self.win = 'AI'
		elif sum(self.AI_hand_val) > 21:
			self.win = 'Player'

	def playerChoice(self):
		choice = raw_input('Hit or Stand?\n>>> ').lower()
		if choice == 'hit':
			self.PL_hand_vis.append(self.deckFunc.deck.pop())
	
	def AIChoice(self):
		hitchance = 10
		if sum(self.AI_hand_val) >= 12:
			hitchance = 8	# 80 %
		if sum(self.AI_hand_val) >= 16:
			hitchance = 4	# 40 %
		if sum(self.AI_hand_val) >= 19:
			hitchance = 1	# 10 %

		chances = []
		for i in range(10):
			if random.randint(1,10) <= hitchance:
				chances.append(True)
			else:
				chances.append(False)

		if random.choice(chances):
			self.AI_hand_val.append(self.deckFunc.deck.pop())

		
if __name__ == '__main__':
	game = BlackJack()