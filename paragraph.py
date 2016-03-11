def div(func):
	def wrapper(*args, **kwargs):
		res = func(*args, **kwargs)
		res = '\n'.join(['\t' + i for i in res.split('\n')])
		return '<div>\n\t' + res + '\n</div>'


	return wrapper

def p(func):
	def wrapper(*args, **kwargs):
		res = func(*args, **kwargs)
		res = '\n'.join(['\t' + i for i in res.split('\n')])
		return '<p>\n' + res + '\n</p>'


	return wrapper

def div(color):
	def wrapper(*args, **kwargs):
		def wrapped(*args, **kwargs):
			res = func(*args, **kwargs)
			res = '\n'.join(['\t' + i for i in res.split('\n')])
			return '<div-style="background-color:#{}">\n'.format(color) + res + '\n<div>'

		return wrapped
	return wrapper

@div('22F')



@p
@div
def greetings(name):
	return "Hello {} <br>\n Nice to meet you!".format(name)

	return wrapper


print greetings('World')

with open('hello.html', 'w') as f:
	f.write(greetings('World'))