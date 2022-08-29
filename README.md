# DOCUMENTATION ON THE API
### the ZOMBIE APOCALYPSE 2090 MODEL

### Over view

	


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

creating transactins for trying out an see results

	>>> trans1 = transactions.Debit(user1, 90)
	>>> trans1.debit()
	'SUCCESS'
	>>> user1.balance
	40

user3 gets $0 balance by default

	>>> user3.balance
	0

performing debit again after low balance

	>>> trans2 = transactions.Debit(user1, 190)
	>>> trans2.debit()
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "C:\SODIQ-DEMO-BANKING\sub\transactions.py", line 66, in debit
	    raise LowBalanceError(f"{self.account}'s balance is not enough for this Transaction")
	errors.LowBalanceError: mark - None's balance is not enough for this Transaction

alse performing bulk transfer on low balance:

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

I have written more unnit test to further cover more edge cases


thanks 

SODIQ
