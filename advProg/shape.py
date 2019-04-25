class Circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        return (self.r**2)*3.14

    def perimeter(self):
        return 2*self.r*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.r, self.area(), self.perimeter())

#My work --

class Rectangle():
	def __init__(self,h,w):
		self.h = h
		self.w = w

	def area(self):
		return self.h*self.w

	def perimeter(self):
		return (2*self.h) + (2*self.w)

	def __str__(self):
		return   """Height: %.2f\nWidth: %.2f\nArea: %.2f\nPerimeter: %.2f""" % (self.h , self.w , self.area() , self.perimeter())


class Triangle():
	def __init__(self,h,w,hyp):
		self.h = h
		self.w = w
		self.hyp = hyp

	def area(self):
		return (self.h*self.w)*0.5

	def perimeter(self):
		return self.h+self.w+self.hyp

	def __str__(self):
		return "Height: %.2f\nWidth: %.2f\nArea: %.2f\nPerimeter: %.2f" %(self.h , self.w, self.area() , self.perimeter())

'''
class Depth():	# integrate these things *into the other classes*
	def __init__(self,depth,shape):
		self.shape = shape
		self.depth = depth
		if shape == Circle():
			self.s = 'circle'
		elif shape == Rectangle():
			self.s = 'Rectangle'

	def surface_area(self):
		if self.s == 'circle':
			return self.shape.area()*4
		elif self.s == 'rectangle':
			return 2*( (self.shape.w*self.depth) + (self.shape.h*self.depth) + (self.shape.h*self.shape.w) )

	def volume(self):
		if self.s == 'rectangle':
			return self.shape.w*self.shape.h*self.depth
		elif self.s == 'circle':
			return 	(4/3)*3.14*(self.shape.r**3)

	def __str__(self):
		return 'Surface Area: %.2f\nVolume: %.2f' %(self.surface_area(),self.volume())
'''