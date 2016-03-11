def b(func):
	def wrapper (*agrs, **kwargs):
		return '<b>' + func(*agrs, **kwargs) + '</br>'

	return wrapper

def i(func):
	def wrapper (*agrs, **kwargs):
		return '<i>' + func(*agrs, **kwargs) + '</i>'

	return wrapper

def div(func):
	def wrapper(*agrs, **kwargs):
		res = func(*argsm, **kwargs)
		res = '\n'.join(['\t' + i for i in res.split('\n')])
		return '<div>\n\t' + res + '\n</div>'


	return wrapper

@i
def greetings(name):
	return "Hello {} <br>\n Nice to meet you!".format(name)

	return wrapper


print greetings('World')

with open('hello.html', 'w') as f:
	f.write(greetings('World'))