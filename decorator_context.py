import sys
from functools import wraps

class MagicalThing(object):

	def __init__(self, entering, exiting):
		self.entering = entering
		self.exiting = exiting
		print "making magical thing"

	def __enter__(self):
		print "do entering"
		self.entering()
		print "did entering"

	def __exit__(self, exc_type, exc_value, traceback):
		print "do exiting"
		self.exiting()
		print "did exiting"

	def __call__(self, func):
		@wraps(func)
		def inner(*args, **kwargs):
			self.__enter__()
			try:
				res = func(*args, **kwargs)
			except:
				self.__exit__(*sys.exc_info())
			finally:
				self.__exit__(None, None, None)
			return res
		return inner	


def decwrapper(entering, exiting, using):
	if callable(using):
		return MagicalThing(entering, exiting)(using)
	else:
		return MagicalThing(entering, exiting)

def mydec(function_or_database_name=None):
	def entering():
		print "Entering"

	def exiting():
		print "Exiting"

	return decwrapper(entering, exiting, using)


@mydec(using="mydb")
def myfunc():
	print "I'm in my func!!!"



if __name__ == '__main__':
	myfunc()
	with mydec(using="ME!!!!"):
		myfunc()


