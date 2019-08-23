class Sorter:
	def __init__(self, data, sort_order):
		self.data = data
		self.order = sort_order
		self.reversed = (sort_order == 'descending')

	def is_float(self, element):
		try:
			float(element)
		except:
			return False
		else:
			return True

	def is_int(self, element):
		try:
			int(element)
		except:
			return False
		else:
			return True
	
	def is_sci_notation(self, element):
		if self.is_int(element) == False and self.is_float(element) and 'e' in element:
			return True
		else:
			return False

	def sort(self):
		pass