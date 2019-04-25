import cardBasics
import random

class Palace:

	debug = True

	playerHand = {}
	player_6 = {}

	AIHand = {}
	AI_6 = {}

	deckExceptions = { 	'Jack' : 11 ,
						'Queen': 12 ,
						'King' : 13 ,
						'Ace'  : 14 }

	deckFunc = cardBasics.Deck(False)

	discard = []

	win = 0

	

	def __init__(self):
		self.deckFunc.shuffle()

		self.initial_Deal()

		while self.win == 0:
			try:
				self.top = self.discard[-1]
			except: 
				self.top = 0	# discard pile empty
			self.AI_play_card()
			self.player_play_card()




	def initial_Deal(self):
		for hand in [self.player_6,self.AI_6]:
			for palaceCards in range(6):
				newCard = self.deckFunc.pile.pop()
				self.add_card_to(hand,newCard)

		for hand in [self.playerHand,self.AIHand]:
			for deal in range(3):
				newCard = self.deckFunc.pile.pop()
				self.add_card_to(hand,newCard)

	def add_card_to(self,hand,newCard):
		try:
			hand[newCard] = int(newCard.split()[0])
		except:
			for face in self.deckExceptions:
				if face in newCard:
					hand[newCard] = self.deckExceptions[face]
					break

	def player_play_card(self):
		playable = []

		for card in self.playerHand.values():
			if card > self.top:
				playable.append(card)

		print 'Here is your current hand:'
		for i in self.playerHand:
			print i

		if playable != []:
			print '\nYou can currently play these values from your hand:'
			for i in playable:
				print i
			cardChoice = input('>>> ')
			for i in self.playerHand:
				if self.playerHand[i] == cardChoice:
					del self.playerHand[i]
					break
			while len(self.playerHand) < 3:
				newCard = self.deckFunc.pile.pop()
				self.add_card_to(self.playerHand,newCard)

			self.discard.append(cardChoice)
		else:
			for card in self.discard:
				self.add_card_to(self.playerHand,card)

		self.top = self.discard[-1]

			

	def AI_play_card(self):
		playable = []

		for card in self.AIHand.values():
			if card > self.top:
				playable.append(card)

		if playable != []:
			del self.AIHand.values()[self.AIHand.values().index(min(playable))]
			while len(self.AIHand) < 3:
				newCard = self.deckFunc.pile.pop()
				self.add_card_to(self.AIHand,newCard)
			
			self.discard.append(min(playable))
			print 'AI played a card worth',min(playable)
		else:
			for card in self.discard:
				self.add_card_to(self.AIHand,card)

		self.top = self.discard[-1]


palace = Palace()