import cardBasics
import random

class War:

	cardValues = [0,1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

	deck = []

	playerPile = []
	AIPile = []
	
	win = 0

	def __init__(self):

		self.make_deck()
		self.deal()

		while self.win == 0:

			x = raw_input('Press Enter to draw. ')
			playerCard = self.playerPile.pop()
			AICard = self.AIPile.pop()
			stakes = [playerCard,AICard]

			print 'Player drew', self.cardValues[playerCard]
			print 'AI drew', self.cardValues[AICard]

			if playerCard > AICard:
				self.player_win(stakes)
			elif playerCard < AICard:
				self.AI_win(stakes)
			elif playerCard == AICard:
				self.draw([])

			self.win_check()

		print self.win,'Wins!'

	def make_deck(self):
		for suit in range(4):
			for face in range(2,11):
				self.deck.append(face)
			for face in ['Jack','Queen','King','Ace']:
				self.deck.append(face)
		random.shuffle(self.deck)
		random.shuffle(self.deck)	

	def deal(self):
		n = 0
		for card in self.deck:
			n += 1
			if n % 2 == 0:
				self.AIPile.append(self.cardValues.index(card))
			else:
				self.playerPile.append(self.cardValues.index(card))

	def player_win(self,stakes):
		for card in stakes:
			self.playerPile.append(card)
		print 'Player won the draw!'

	def AI_win(self,stakes):
		for card in stakes:
			self.AIPile.append(card)
		print 'AI won the draw.'

	def draw(self,stakes):
		for i in range(3):
			stakes.append(self.cardValues.index(self.playerPile.pop()))
		for i in range(3):
			stakes.append(self.cardValues.index(self.AIPile.pop()))

		if stakes[5] > stakes[2]:
			self.AI_win(stakes)
		elif stakes[5] < stakes[2]:
			self.player_win(stakes)
		elif stakes[5] == stakes[2]:
			self.draw(stakes)

	def win_check(self):
		if len(self.playerPile) == 0:
			self.win = 'AI'
		elif len(self.AIPile) == 0:
			self.win = 'Player'

war = War()