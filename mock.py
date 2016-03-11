import mock

# class User(object):
# 	def __init__(self, name, year):
# 		self.name = name
# 		self.year = year

# user = User('Oksana', 2012)

# mock_user = mock.Mock(user)
# # mock_user.name = 'Oksana'
# # mock_user.year = 2012



def f():
	print 'f() called'

a = mock.Mock(side_effect=f)

print a()

# mail
# virtualenv

# http://use-the-index-luke.com/
# Learning Python / Lutz
# The Hacker's Guide to Python / Julien Danjou
# Fluent Python / Luciano Ramalno
# RISE University
# codecademy.com
# coursera.com
