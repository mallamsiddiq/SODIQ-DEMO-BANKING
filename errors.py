class LowBalanceError(Exception):
	'''Raise if a balasnce-required event is called on insufficient balance account'''

class RecipientError(Exception):
	'''Raise if a recipient-needed event is called with no or wrong recipient'''