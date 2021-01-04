#This is a simple library to scale values to/from decimals between 0 and 1.

def netmin(arr):
	retval=arr
	while type(retval)!=int and type(retval)!=float:
		retval=min(retval)
	return retval
def netmax(arr):
	retval=arr
	while type(retval)!=int and type(retval)!=float:
		retval=max(retval)
	return retval
class Scaler:
	def __init__(self, minval=None, maxval=None):
		self.min=minval
		self.max=maxval
		try:
			self.coefficient=1/(self.max-self.min)
			self.offset=self.min-0
		except:
			pass
	def setscale(self, samples, leeway=0):
		self.min=netmin(samples)-float(leeway)
		self.max=netmax(samples)+float(leeway)
		self.coefficient=1/(self.max-0)
		self.offset=self.min-0
	def scaleto(self, value):
		return self.coefficient*(value-self.offset)
	def scalefrom(self, value):
		return value/self.coefficient+self.offset
	def scaleset(self, x):
		retx=x
		for i, val in enumerate(x):
			retx[i]=self.scaleto(val)
		return retx
	def scaleback(self, x):
		retx=x
		for i, val in enumerate(x):
			retx[i]=self.scalefrom(val)
		return retx
	def scalestuff(self, stuff):
		retx=stuff
		for i, val in enumerate(stuff):
			retx[i]=self.scaleset(val)
		return retx

