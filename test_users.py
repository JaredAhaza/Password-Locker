import unittest
from user import User

class TestUser(unittest.TestCase):

	@classmethod
	def SetupUserClass(cls):
		"""
        sets up the user class
        """
		print("setup class")

	@classmethod
	def tearDownClass(cls):
		"""
        runs after each test
        """
		print("teardown class")

	def setUp(self):
		"""
        sets up the data needed to test User class
        """
		self.user1 = User("user", "jare2000")
		self.user2 = User('new user',"jare2000")
		
	def test_init(self):
		"""
        checks whether instances have been well created
        """
		self.assertEqual(self.user1.username, 'user')
		self.assertEqual(self.user1.login_password, "jare2000")
	def tearDown(self):
		User.users = dict()
		""" run to clean up the class"""
	@classmethod
	def list_users(cls):
		print("hello")

if __name__ == '__main__':
	print("testing")
	unittest.main()