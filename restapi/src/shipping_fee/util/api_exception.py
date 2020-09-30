from flask import abort


class ApiException:

	@staticmethod
	def handle(func):

		def wrapper(*args, **kwargs):

			try:
				val = func(*args, **kwargs)
				return val
			except:
				return abort(400)

		wrapper.__name__ = func.__name__
		return wrapper


