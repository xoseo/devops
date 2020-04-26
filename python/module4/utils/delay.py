from time import sleep

def delay(func):
	def wrapper(*args, **kwargs):
		sleep(3)
		return func(*args, **kwargs)
	wrapper.__name__ = func.__name__
	wrapper.__doc__ = func.__doc__
	return wrapper

