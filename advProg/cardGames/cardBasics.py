import random
class Deck:

	def __init__(self,includeJokers):
		self.deck = []
		self.create(includeJokers)
		self.pile = self.deck

	def create(self,includeJokers):
		for suit in ['Spades','Clubs','Hearts','Diamonds']:
			for num in range(2,11):
				self.deck.append(str(num)+' of_'+suit)
			for face in ['Ace','Jack','Queen','King']:
				self.deck.append(face+' of_'+suit)
		if includeJokers:
			for i in range(2):
				self.deck.append('Joker')

	def shuffle(self):
		random.shuffle(self.pile)


if __name__ == '__main__':
	deckA = Deck(True)
	deckA.shuffle()
	print 'fulldeck:',len(deckA.pile)
	print deckA.deal(3)
	print 'pile:',len(deckA.pile)
	print 'deck',len(deckA.deck)
