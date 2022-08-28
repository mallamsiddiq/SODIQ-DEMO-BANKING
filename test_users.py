from users import User
import unittest

class UserTest(unittest.TestCase):
	
	def setUp(self):

		self.user1 = User('adebakin', 40)
		self.user2 = User('racheal', )
		self.user3 = User('ushra', 200)
		self.user4 = User('mark', 20)
		self.user5 = User('leeha', 25)
		self.user6 = User('temi')
		self.user7 = User('shola', 25)

		self.allusers=[self.user1, self.user2, self.user3, self.user4, self.user5, self.user6, self.user7]

	def test_user_create_attr(self):

		self.assertListEqual([self.user1.fullname, self.user1.balance], ['adebakin', 40])
		self.assertListEqual([self.user2.fullname, self.user2.balance], ['racheal', 0])
		self.assertNotEqual([self.user3.fullname, self.user3.balance], ['ushrat', 200])
		self.assertListEqual([self.user4.fullname, self.user4.balance], ['mark', 20])
		self.assertNotEqual([self.user5.fullname, self.user5.balance], ['leeha', 15])
		self.assertNotEqual([self.user6.fullname, self.user6.balance], ['temi', 30])
		self.assertListEqual([self.user7.fullname, self.user7.balance], ['shola', 25])

	def test_user_repr(self):

		for user in self.allusers:
			self.assertEqual(f"{user.fullname} - {user.id}", str(user))




if __name__ == '__main__':

	unittest.main()