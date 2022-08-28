class User:

	def __init__(self, fullname, balance = 0 ):

		self.balance = balance

		self.fullname = fullname

		self.id = None

	def __str__(self):

		return f"{self.fullname} - {self.id}"