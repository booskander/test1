def imprimer():
	print("Hello from py")
	
class MaClasse:
	def __init__(self, a, b, c):
		self.nom = a
		self.age = b
		self.matricule = c
		
	def afficher(self):
		print(self.nom)
		print(self.age)
		print(self.matricule)
		
	def getNom(self):
		return self.nom
