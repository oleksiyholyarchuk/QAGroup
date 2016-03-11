from registryvsdecorator import User, Item, Order

def loyalty_discount(order):
	if order.user.years  > 10:
		return 0.05 * order.cost
	else:
		return 0

def big_cost_discount(order):
	if order.cost > 1000:
		return 0.04 * order.cost
	else:
		return 0

def bulk_discount(order):
	if order.max_single_count > 100:
		return 0.1 * order.cost
	else:
		return 0


def distinct_discount(order):
	if order.distinct_discount >= 5:
		return 0.04 * order.cost
	else:
		return 0

def best_discount(order):
	return max([loyalty_discount(order),
				big_cost_discount(order),
				bulk_discount(order),
				distinct_discount(order)])

if __name__ == '__main__':
	user = User('Ivan', 2000)
	order = Order(user, {Item('Pen', 100):1})
	assert loyalty_discount(order) == 5
	user.year_registered = 2013
	assert loyalty_discount(order) == 0

	assert big_cost_discount(order) == 0
	order = Order(user, {Item('Pen', 100):20})
	print big_cost_discount(order) == 80

	assert bulk_discount(order) == 0
	order = Order(user, {Item('Pen', 1):200})
	assert bulk_discount(order) == 20

# promotion (...) -> 0.2