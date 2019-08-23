from sorter import Sorter
from decimal import * 

class NumSorter(Sorter):
	""" child class for numeric sorting operations on lists

	Attributes:
		inherited from parent Sorter
	"""
	def __init__(self, data, sort_order):
		super().__init__(data, sort_order)

	def data_trim_strings(self, input_data):
		output_data = []
		for row in input_data:
			output_row = []
			for el in row:
				if self.is_float(el) or self.is_int(el) or self.is_sci_notation(el):
					output_row.append(el)
			output_data.append(output_row)

		return output_data
	
	def sort_on_float(self, x):
		""" key to define the sorting rules, convert sci_notations into 
			decimals and sort, but maintain its sci_notations format 
			avoided the problem with treating it as alphabetical in sorting 
		"""
		return Decimal(x)

	def sort(self):
		""" Similar approach as the AlphaSorter 
		"""
		new_data = self.data_trim_strings(self.data)
		sorted_data = [sorted(row, key=self.sort_on_float, reverse=self.reversed) for row in new_data]
		result = [', '.join(row) for row in sorted_data]
		
		return result