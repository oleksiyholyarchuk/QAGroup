#d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
#x = obj(d)
#x.b.c



#class A(object)
#	def __init__(self, container):
#		self.container = container
#	def __getitem__(self, name):
#		return self.container[name]

a = AttrDict()
a['key1'] = 'value1'
a.key1