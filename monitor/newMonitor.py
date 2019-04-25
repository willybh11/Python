import psutil
import turtle

def main():
	monitor = Monitor()	# initialize class
	monitor.run()		# run it

class Monitor(object):

	def __init__(self):

		self.windowSetup()	# setup window and borders
		self.clearGraph()	# set up graph lines
		self.init_var()		# set up turtles

	def run(self):

		while 1:
			self.refreshBars()	# refresh bar data
			self.refreshGraph()	# refresh graph data

	def refreshBars(self):
		self.cpu_multi = psutil.cpu_percent(interval=1, percpu=True)	# [cpu1,cpu2,cpu3,cpu4]
		self.updateBars()		# draw new bars using cpu_multi

	def updateBars(self):
		box = turtle.Turtle()

		for edit in ['erase','draw']:	# erase existing bars, then draw new ones
			box.fillcolor('blue' if edit == 'draw' else 'white')	# erase = draw over with white
			box.ht()

			for cpuNum in range(4):	# for each cpu
				if edit == 'draw':	# if drawing, find num of bars to draw
					cpuStrain = self.cpu_multi[cpuNum]	# iniv cpu strain

					for i in range(10,0,-1):	# back from 10 to 0 by -1
						if cpuStrain / 10 <= i:	# find where the last bar will be
							barsToDraw = i
						else:	break			#break the for loop and stop searching

				for bars in range(barsToDraw if edit == 'draw' else 10):
					box.pu()
					xcoord = -640 + (325*cpuNum)	# specific y-coord
					ycoord = 10 + (32*bars)			# specific x-coord
					box.goto(xcoord,ycoord)
					box.pd()

					box.begin_fill()

					for side in range(2):	# draw the box
						box.fd(305)
						box.lt(90)
						box.fd(22)
						box.lt(90)

					box.end_fill()
				turtle.update()		# refresh screen

	def refreshGraph(self):
		self.cpu_avg = psutil.cpu_percent()		# new cpu ycoord
		self.vram = psutil.virtual_memory()[2]	# new vram ycoord
		self.swap = psutil.swap_memory()[3]		# new swap ycoord

		self.updateGraph()	#implement above data

	def updateGraph(self):
		markers = {	self.cpu_marker  : self.cpu_avg ,	# turtle : its new y-value
					self.vram_marker : self.vram , 
					self.swap_marker : self.swap }

		for marker in markers:
			old_x = marker.xcor()
			old_y = marker.ycor()

			new_x = old_x + 65	# will fit 20 datapoints in one graph	
			new_y = -330 + (markers[marker] * 3.3)	# go to corresponding y-coord
			
			if new_x > 650:			# if at the end of the graph:
				self.clearGraph()	# clear it
				self.init_var()		# re-initialize variables
				break

			marker.goto(new_x,new_y)	# goto new coords (if not reset)

	def clearGraph(self):			
		reset = turtle.Turtle()
		reset.pencolor('gray')		# to draw lines
		reset.fillcolor('white')	# to 'erase' the graph
		reset.ht()
		reset.pu()
		reset.goto(-649,-339)		# go to origin (1 pixel off not to erase the borders)
		reset.begin_fill()
		for i in range(2):			# draw the box
			reset.fd(1299)
			reset.lt(90)
			reset.fd(329)
			reset.lt(90)
		reset.end_fill()
		for line in range(0,10):	# draw the new lines
			if line == 0:	reset.pencolor('black')	# first line must be black (fill issue)
			else:			reset.pencolor('gray')
			reset.goto(-650,-330 + (33 * line))		# goto new line pos
			reset.pd()
			reset.fd(1300)	# draw the actual line
			reset.pu()

	def init_var(self):
		self.cpu_marker  = turtle.Turtle()
		self.vram_marker = turtle.Turtle()
		self.swap_marker = turtle.Turtle()

		pencolors = { 	self.cpu_marker  : 'blue',		# indiv. line color for later referrence
						self.vram_marker : 'red' ,
						self.swap_marker : 'orange' }

		for marker in pencolors.keys():	# repeat per marker
			marker.ht()
			marker.pensize(2 if marker == self.swap_marker else 3)	# swap is smaller because it mostly stays at 0
			marker.pencolor(pencolors[marker])	# set corresponding pencolor
			marker.pu()
			marker.goto(-650,-330)	# go to origin
			marker.pd()


	def drawBox(self,pos,h,w):	# starts at bottom left of box
		self.box.pu()
		self.box.goto(pos)
		self.box.pd()
		for i in range(2):
			self.box.fd(w)
			self.box.lt(90)
			self.box.fd(h)
			self.box.lt(90)

	def windowSetup(self):
		self.window = turtle.Screen()
		self.window.setup()#coords#
		self.box = turtle.Turtle()

		self.drawBox((0,0),300,50)

		# new graphics:
		#	four columns of circles for CPU
		#	graph ....... somewhere
		#		maybe smaller graphs in rows?



		'''
		self.window = turtle.Screen()
		self.window.setup(1365,720)	# my old resolution

		borders = turtle.Turtle()
		borders.tracer(0,0)
		borders.ht()
		borders.pu()
		borders.goto(-650,-330)	# go to origin
		borders.pd()
		for i in range(2):		# draw main box
			borders.fd(1300)
			borders.lt(90)
			borders.fd(660)
			borders.lt(90)
		borders.lt(90)			#
		borders.fd(330)			# (-650,0)
		borders.rt(90)			#
		for i in range(4):		# draw cpu boxes
			borders.fd(325)
			borders.lt(90)
			borders.fd(330)
			borders.bk(330)
			borders.rt(90)
		turtle.update()			# refresh screen
		'''


if __name__ == '__main__':
	main()


