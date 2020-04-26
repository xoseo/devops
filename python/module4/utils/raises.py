def raises(custom_exception):
	def decorator(func):
		def wrapper(*args, **kwargs):
			try:
				func(*args, **kwargs)
			except Exception as err:
				raise custom_exception()
		return wrapper
	return decorator
