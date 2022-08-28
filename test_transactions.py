from errors import LowBalanceError, RecipientError
from users import User
from transactions import Transfer, CheckBalance, Debit, Deposit
import unittest

class TransactionsTest(unittest.TestCase):

	def setUp(self):

		self.user1 = User('adebakin', 200)
		self.user2 = User('racheal', )
		self.user3 = User('ushra', 40)
		self.user4 = User('mark', 20)

	def test_transfer_success(self):

		# bulk transfer multiple Recipient
		trans = Transfer(self.user1, 45, self.user2, self.user3, self.user4)

		response = trans.transfer()

		self.assertEqual(response, "SUCCESS")
		self.assertEqual(self.user1.balance, 200 - 45 * 3) # confirming debited account
		self.assertEqual(self.user2.balance, 45 + 0) # confirming credited account
		self.assertEqual(self.user3.balance, 45 + 40) # confirming credited account
		self.assertEqual(self.user4.balance, 45 + 20) # confirming credited account


		with self.assertRaises(LowBalanceError):
			# expecting errorr raise for insufficient fund after massive debit
			trans.transfer() 

		with self.assertRaises(LowBalanceError):
			# expecting errorr raise for insufficient fund for exccessive fund transfer
			Transfer(self.user3, 645, self.user2, self.user3, self.user4).transfer() 

		# single Recipient transaction 
		trans2 = Transfer(self.user3, 50, self.user1)
		response2 = trans2.transfer()

		self.assertEqual(response, "SUCCESS")

		# confirming credited account
		self.assertEqual(self.user1.balance, 65 + 50 ) 

		# confirming debited account
		self.assertEqual(self.user3.balance, 45 + 40 -50)


	def test_transfer_no_recpt(self):

		with self.assertRaises(RecipientError):
			# expecting RecipientError raised for not providing Recipient
			Transfer(self.user1, 45).transfer()

	def test_deposit(self):

		trans = Deposit(self.user1, 50)

		response = trans.deposit()

		self.assertEqual(response, "SUCCESS")
		self.assertEqual(self.user1.balance, 200 + 50)

	def test_debit(self):

		trans = Debit(self.user1, 150)

		response = trans.debit()

		self.assertEqual(response, "SUCCESS")
		self.assertEqual(self.user1.balance, 200 - 150)

		trans2 = Debit(self.user1, 150)

		with self.assertRaises(LowBalanceError):
			# expecting errorr raise for insufficient fund after massive debit
			trans2.debit() 
	def test_balance_query(self):

		trans = CheckBalance(self.user1)

		balance = trans.checkbalance()

		self.assertEqual(balance, 200)


if __name__ == '__main__':

	unittest.main()