class Sorter:
	""" Parent class for sorting operations on lists

	Attributes:
		data (list): list of lists of values to be sorted
		sort_order (string): the sort order, either ascending or descending
	"""
	def __init__(self, data, sort_order):
		self.data = data
		self.order = sort_order
		self.reversed = (sort_order == 'descending')

	def is_float(self, element):
		""" Determine if the input string is convertible to a float

		Args:
			element (string): the input element to be examined
		Raises:
			ValueError: return False, it's a pure string and can't be converted to a float
		Returns:
			boolean: if the string is convertible to float
		"""
		try:
			float(element)
		except:
			return False
		else:
			return True

	def is_int(self, element):
		""" Similar to is_float but determines if the input string is convertible to an int
		"""
		try:
			int(element)
		except:
			return False
		else:
			return True
	
	def is_sci_notation(self, element):
		""" Determine if the input string is a scientific notation
		"""
		if self.is_int(element) == False and self.is_float(element) and 'e' in element:
			return True
		else:
			return False

	def sort(self):
		""" sorting method to be implemented by child classes
		"""
		pass