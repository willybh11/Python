import random

class Palace:

	cardValues = [0,1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

	deck = []

	playerHand = []
	player_6 = []

	AIHand = []
	AI_6 = []

	discard = []

	win = 0

	

	def __init__(self):

		self.make_deck()
		self.initial_deal()

		while self.win == 0:
			try:
				self.top = self.discard[-1]
			except: 
				self.top = 0	# discard pile empty
			self.AI_play_card()
			self.player_play_card()


	def make_deck(self):
		for suit in range(4):
			for face in range(2,11):
				self.deck.append(face)
			for face in ['Jack','Queen','King','Ace']:
				self.deck.append(face)
		random.shuffle(self.deck)
		random.shuffle(self.deck)	

	def initial_deal(self):
		for hand in [self.player_6,self.AI_6]:
			for palaceCards in range(6):
				hand.append(self.deck.pop())

		for hand in [self.playerHand,self.AIHand]:
			for deal in range(3):
				hand.append(self.deck.pop())

	def player_play_card(self):
		playable = []

		for card in self.playerHand:
			if self.cardValues.index(card) >= self.cardValues.index(self.cardValues[self.top]):
				playable.append(card)

		print 'HAND:',
		for i in self.playerHand:
			print i,

		if playable != []:
			print '\nYou can currently play the following values from your hand:'
			for i in playable:
				print self.cardValues.index(i)
			cardChoice = input('>>> ')
			del self.playerHand[self.playerHand.index(self.cardValues[cardChoice])]
			while len(self.playerHand) < 3:
				newCard = self.deck.pop()
				print 'You drew',newCard
				self.playerHand.append(newCard)

				self.playerHand.append(self.deck.pop())
			self.discard.append(cardChoice)
		else:
			print 'You cant play anything.'
			for card in self.discard:
				newCard = self.deck.pop()
				print 'You drew',newCard
				self.playerHand.append(newCard)
		self.top = self.discard[-1]

	def AI_play_card(self):
		playable = []

		for card in self.AIHand:
			if card >= self.top:
				playable.append(card)

		if playable != []:
			del self.AIHand[self.AIHand.index(min(playable))]
			while len(self.AIHand) < 3:
				self.AIHand.append(self.deck.pop())
			
			self.discard.append(min(playable))
			print 'AI played',min(playable),'( worth',self.cardValues.index(min(playable)),')'
		else:
			for card in self.discard:
				self.AIHand.append(self.deck.pop())

		self.top = self.discard[-1]


palace = Palace()