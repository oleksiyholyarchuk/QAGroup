import unittest
from registryvsdecorator import User, Order, Item
from testing import loyalty_discount, bulk_discount, big_cost_discount, distinct_discount

#preparation for text execution (fixture)

class LoyaltyDiscountTastCase(unittest.TestCase):
	def test_positive(self):
		user = User('Ivan', 2000)
		order = Order(user, {Item('Pen',100): 1})
		self.assertEqual(loyalty_discount(order),5)

	def test_zero(self):
		user = User('Ivan', 2000)
		order = Order(user, {Item('Pen',100): 1})
		self.assertEqual(loyalty_discount(order),0)

class BulkDiscountTestCase(unittest.TestCase):

	def setUp(self):
		self.user = User('Ivan', 2014)

	#def tearDown()

	def test_positive(self):
		order = Order(self.user, {Item('Pen',1): 200})
		self.assertEqual(bulk_discount(order),0)

	def test_zero(self):
		order = Order(self.user, {Item('Pen',200): 1})
		self.assertEqual(bulk_discount(order),0)

class BigDiscountTestCase(unittest.TestCase):

	def setUp(self):
		self.user = User('Ivan', 2014)

	def test_positive(self):
		order = Order(self.user, {Item('Pen',100): 20})
		self.assertEqual(big_cost_discount(order), 80)

	def test_zero(self):
		order = Order(self.user, {Item('Pen',10): 20})
		self.assertEqual(big_cost_discount(order), 0)

class DistinctDiscountTestCase(unittest.TestCase):

	def setUp(self):
		self.user = User('Ivan', 2014)

	def test_positive(self):
		order = Order(self.user, {Item('Pen',1): 1,
								  Item('Pencil',1): 1,
								  Item('Marker',1): 1,
								  Item('Notebook',1): 1,
								  Item('Book',96): 1})
		self.assertEqual(distinct_discount(order),4)

	def test_zero(self):
		order = Order(self.user, {Item('Pen',200): 1})
		self.assertEqual(bulk_discount(order),0)

class BestDiscountTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User('Ivan', 2014)

	def test_best(self):
		order = Order( self.user, {Item('Pen',1): 1,
								  Item('Pencil',1): 1,
								  Item('Marker',1): 1,
								  Item('Notebook',1): 1,
								  Item('Book',96): 1})
		self.assertEqual(best_discount(order),0)
