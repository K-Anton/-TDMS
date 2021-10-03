
class Field:
	def __init__(self, name_, value_=None):
		self.__name = name_
		self.__value = value_
	
	def get_name(self):
		return self.__name
	
	def get_value(self):
		return self.__value.get_value()

	def set_name(self, name_):
		self.__name = name_

	def set_value(self, value_):
		self.__value = value_
