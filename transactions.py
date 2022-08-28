
from errors import LowBalanceError, RecipientError
import datetime

class Transaction:

	def __init__(self):

		self.date = datetime.datetime.now()
		self.id = None
		self.success = True

class Transfer(Transaction):

	def __init__(self, sender, amount, *recipients):
		super().__init__()
		self.sender = sender
		self.amount = amount
		self.recipients = recipients

	def transfer(self):

		if not self.recipients:

			raise RecipientError("[no recipient provided]")

		if self.sender.balance >= self.amount * len(self.recipients):

			for recipient in self.recipients:
				recipient.balance += self.amount

			self.sender.balance -= self.amount * len(self.recipients)

			return "SUCCESS"

		self.success = False
		raise LowBalanceError(f"[{self.sender}'s balance is not enough for this Transaction]")


class Deposit(Transaction):

	def __init__(self, account, amount):
		super().__init__()
		self.account = account
		self.amount = amount

	def deposit(self):
		self.account.balance += self.amount
		return "SUCCESS"


class Debit(Transaction):

	def __init__(self, account, amount):
		super().__init__()
		self.account = account
		self.amount = amount

	def debit(self):

		if self.account.balance >= self.amount:
			self.account.balance -= self.amount
			return "SUCCESS"

		self.success = False
		raise LowBalanceError(f"{self.account}'s balance is not enough for this Transaction")


class CheckBalance(Transaction):

	def __init__(self, account):
		super().__init__()
		self.account = account

	def checkbalance(self):
		return self.account.balance


