import cardBasics



class BlackJack:

	debug = True

	def __init__(self):
		self.deck = cardBasics.Deck(False)
		self.deck.shuffle()

		if self.debug: print self.deck



if __name__ == '__main__':
	game = BlackJack()