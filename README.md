# dOc [please, Read ME]

### the MOCK BACKEND FOR A PEER TO PEER PAYMENT API

### Overview

I have created a mock simulation of the banking backend logic, one you can interact with via python console. 

So right in this root directory you can make a call to the module Objects: User from users.py and [ Transfer, Debit, CheckBalance, Deposit] from transaction.py with the following signatures for instantiation:

	Transfer(self, sender, amount, *recipients):

	Deposit(self, account, amount):

	Debit(self, account, amount):

	CheckBalance( self, account):

	User(self, fullname, balance = 0 ):

all transactions extend from the base Transaction class i created.

I also created two custom errors both extends built-in python Extension

	LowBalanceError
	'''Raise if a balance-required event is called on insufficient balance account'''

	RecipientError
		'''Raise if a recipient-needed event is called with no or wrong recipient'''

## TESTING 

I have written unittest that covers edge corner cases

in the root directory simply run

	python -m unittest		

### Interacting with VIA python console

see below how i did a little simulation of the logics

	>>> import users
	>>> import transactions
	>>> user = users.User
	>>> user0 = user('hjh', 67)
	>>> user0
	<users.User object at 0x00000222AF773400>
	

initiating four users

	>>> user2 = user('hikmot', 67)
	>>> user1 = user('mark', 67)
	>>> user1 = user('mark', 130)
	>>> user3 = user('mark')
	>>> user4 = user('mark', 45)

user1 requesting a debit transactions

	>>> trans1 = transactions.Debit(user1, 90)
	>>> trans1.debit()
	'SUCCESS'
	>>> user1.balance
	40

user3 gets $0 balance by default since no balance provided at creation

	>>> user3.balance
	0

user1 performing debit again after low balance

	>>> trans2 = transactions.Debit(user1, 190)
	>>> trans2.debit()
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "C:\SODIQ-DEMO-BANKING\sub\transactions.py", line 66, in debit
	    raise LowBalanceError(f"{self.account}'s balance is not enough for this Transaction")
	errors.LowBalanceError: mark - None's balance is not enough for this Transaction

also performing bulk transfer on low balance from user1 to user 2 - 4

	>>> trans3 = transactions.Transfer(user1, 100, user2, user3, user4)
	>>> trans3.transfer()
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "C:\Users\SODIQ\webapps\SODIQ-DEMO-BANKING\sub\transactions.py", line 37, in transfer
	    raise LowBalanceError(f"{self.account}'s balance is not enough for this Transaction")
	errors.LowBalanceError: mark - None's balance is not enough for this Transaction



user1 trying to send money without providing recipients


	>>> trans5 = transactions.Transfer(user1, 30)
	>>> trans5.transfer()
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		  File "C:\SODIQ-DEMO-BANKING\sub\transactions.py", line 25, in transfer
		    raise RecipientError("[no recipient provided]")
		errors.RecipientError: [no recipient provided]

then user4 checks his balance and transfer some fund to user1:

	
	>>> user4.balance
		105
	>>> trans6 = transactions.Transfer(user4, 30, user1)
	>>> trans6.transfer()
		'SUCCESS'

user1 make a deposit 0f $30 and check his balance

	>>> trans7 = transactions.Deposit(user1, 30)
	>>> trans7.deposit()
		'SUCCESS'
	>>> trans8 = transactions.CheckBalance(user1)
	>>> trans8.checkbalance()
		70


user1 now transfer $15 to the rest user and $10 separate to user3 

	>>> trans8 = transactions.Transfer(user1, 15, user2, user3, user4)
	>>> trans8.transfer()
		'SUCCESS'

	>>> trans9 = transactions.Transfer(user1, 15, user3)
	>>> trans9.transfer()
		'SUCCESS'

I have written more unit test to further cover more edge cases


thanks 

SODIQ


further complaints to @mallamsiddiq@gmail.com

