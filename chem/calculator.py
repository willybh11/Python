
class MoleCalc:

	def __init__(self): # split the reactants by " ", then look for digits on the LEFT (coefficient) an then on the RIGHT (subtext)

		self.var = {"G":0,	# mass
					"V":0,	# volume
					"P":0,	# particles
					"M":0,	# moles
					"mm":0}	# molar mass

		self.coefficients = {	"G":0				, # for conversion in self.findMoles()
							 	"V":22.4			,
							 	"P":6.02e23			,
							 	"M":1				}

		self.newElements = {}	# any user-input elements go here
		self.masses = {}		# masses from molarmasses.txt go here
		self.reactants = {}

		self.getElements()
		self.askForInput()
		self.compute()
		self.printValues()

	def printValues(self):
		print "\n\t*** %s ***\n" 			%(self.compound)
		print "Mass: .........%.2E (g)" 	%(self.var["G"])
		print "Molar Mass: ...%.2E (g)" 	%(self.var["mm"])
		print "Volume: .......%.2E (L)" 	%(self.var["V"])
		print "Particles: ....%.2E (part)" 	%(self.var["P"])
		print "Moles: ........%.2E (mol)\n" %(self.var["M"])

	def compute(self):
		print self.elements
		for e in self.elements:
			self.analyze(e)
		self.var["M"] = self.var[self.given] / self.coefficients[self.given]
		self.var["G"] = self.var["mm"] * self.var["M"]
		self.var["V"] = self.var["M"]  * self.coefficients["V"]
		self.var["P"] = self.var["M"]  * self.coefficients["P"]

	def askForInput(self):
		self.given = ["V","P","G","M"][input("You are given the:\n1) Volume\t(L)\n2) Particles\t(part)\n3) Mass\t\t(g)\n4) Moles\t(mol)\n>>> ") - 1]
		self.var[self.given] = input("Amount:\n>>> ")
		self.compound = raw_input("Compound: (put spaces between elements please)\n>>> ")
		self.target = "M" if self.given != "M" else "G"
		self.elements = self.compound.split(" ")

	def analyze(self,element):
		symbol = ""
		multiplier = ""
		# element.split("_")
		# if len(element) == 1:
		# 	print "no subtext found"
		# 	element = [element,"1"]
		for character in element:
			if character.isalpha():
				symbol += character
			else:
				multiplier += character

		if multiplier == "": multiplier = "1"

		try:
			for i in range(int(multiplier)):
				self.var["mm"] += self.masses[symbol]
		except:
			self.newElements[symbol] = input("I am not aware of the molar mass of '%s'.\nTell me so I can remember in later questions:\n>>>" %(symbol))
			self.addElements()
			self.analyze(element)

		self.coefficients["G"] = self.var["mm"]

	def addElements(self):
		with open("molarmasses.txt","r+") as f:
			elements = f.readlines()
			for e in self.newElements:
				f.write("\n"+e+":"+str(self.newElements[e]))
		self.newElements = {}
		self.getElements()

	def getElements(self):
		with open("molarmasses.txt","r") as f:
			elements = f.readlines()
			for e in elements:
				e.split(":")
				self.masses[e[0:2].strip(":")] = float(e[e.index(":")+1:])

class SolutionCalc:

	def __init__(self):

		self.var = [0,0,0] #amount, total, molarity

	def askForInput(self):
		print "Type in the value, and then the units.\n\nex. 340 mL\nex. 12 g\nex. 3.4 %\nex. 5 m\n\nLeave the unknown as 'x', and make sure to put the units after it.\n\nex. x g\n\nSupported units: L, mL, g, m, %.\n"
	    self.raw = [raw_input("Amount of Solute: ").upper(),raw_input("Solution Total: ").upper(),raw_input("Molarity %: ").upper()]

	def convert(self):
		for i in range(len(self.raw)):
			if self.raw[i][0] == 'x':
				self.var[i] = 'x'
				self.unkown = ["Amount","Total","Molarity"][i]
			else:
				x = self.raw[i]




if __name__ == "__main__":
	calc = MoleCalc()
