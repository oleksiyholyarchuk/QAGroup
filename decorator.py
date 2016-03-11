# Simple profiler
from datetime import datetime as dt
from time import sleep


def profile(func):
    def wrapper(*args, **kwargs):
        start = dt.now()
        func(*args, **kwargs)
        print '{} finished in {}'.format(func.__name__, dt.now() - start)
    return wrapper


@profile
def slow_talker(phrase):
    sleep(1)
    return 'Talker saaaay {}'.format(phrase)

#slow_talker(1)
a = slow_talker(1)
a == 'Talker saaaay 1'
print a
