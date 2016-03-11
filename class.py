#class A():
#    x = 1
    
#class B(A):
#    y = 20
    
#class C(A):
#   x = 3
#   y = 30
    
#class D(B, C):
#    pass

#d = D()
#print d.x, d.y

#x = AttrDict()
#x['key1'] = 'value1'
#x['key1']
#'value1'

#>>> x.key1
#'value1'

#>>> x.key2 = 'value2'

#>>> x
#{'key1': 'value1', 'key2': 'value2'}

class Practice (Object):
	def __init__(self, )




from random import randint

class PandoraBox(object):
    def __init__(self, limit):
        self.limit = limit
        
    def __getitem__(self, name):
        return randint(0, self.limit)
    
    def __setitem__(self, name, value):
        raise Exception('You cannot put data into Pandora Box')
        
box = PandoraBox(100)
print box[1]
print box[1]
print box['abc']
box[12] = 'data'

