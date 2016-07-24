class Foo:
	def pr(self):
		print "sdfs"

class Pokemon:
	'this classs contains info about pokemons'

	def  __init__(self,name,cp,type):
		self.name=name
		self.cp=cp
		self.type=type

	def displayInfo(self):
		print "My pokemon is %s of type %s with cp %s"%(self.name,self.type,self.cp) 

if __name__=="__main__":
	pikachu=Pokemon("Pikachu",100,"electricity")
	pikachu.displayInfo()
	f=Foo()
	f.pr()
	print type(pikachu)
	print dir(pikachu)
	print pikachu.__doc__
	print pikachu.__module__.__doc__
	



