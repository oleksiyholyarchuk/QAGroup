import unittest
from registryvsdecorator import User, Item

# self.assertRaises (tests whether code we wrote - is raising any exception)
# self.asertRaises(TypeError, User, ('Ivan'), 2014)

class UserTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User('Ivan', 2002)

	def test_name(self):
		self.assertEqual(self.user.name,'Ivan')

	def test_year_registered(self):
		self.assertEqual(self.user.year_registered, 2002)

	def test_years(self):
		self.assertEqual(self.user.years, 13)

class ItemTestCase(unittest.TestCase):
	def test_attributes(self):
		pen = Item('Pen',1)
		self.assertEqual(pen.name, 'Pen')
		self.assertEqual(pen.price, 1)

class OrderTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User('Ivan', 2002)

	def test_attributes(self):
		order = Order(self.user, {Item('Pencil', 0.5):1, Item('Marker', 1.2):2})
		self.assertEqual(order.user.name, 'Ivan')
		self.assertEqual(len(order.items), 2)

	def test_cost(self):
		order = Order(self.user, {Item('Pencil', 0.5):1, Item('Marker', 1.2):2})
		self.assertEqual(order.max_single_count,2)

	def test_max_single_count(self):
		order = Order(self.user, {Item('Pencil', 0.5):1, Item('Marker', 1.2):2})
		self.assertEqual(order.max_single_count,2)

	def test_max_equal_single_count(self):
		order = Order(self.user, {Item('Pencil', 0.5):1, Item('Marker', 1.2):2})
		self.assertEqual(order.max_single_count,2)

	def test_distinct_discount(self):
		order = Order(self.user, {Item('Pencil',0.5):2})
		self.assertEqual(order.distinct_count, 1)
		order = Order(self.user, {Item('Pencil',0.5):2}, {Item('Pen', 1):1}, {Item('Book',10):2})
		self.assertEqual(order.distinct_count, 3)

if __name__ == ('__main__'): # (verbosity)
	unittest.main(verbosity=1)

	#user = User('Ivan', 2002)
	#assert user.name == 'Ivan'
	#assert user.year_registered == 2002
	#assert user.years == 13