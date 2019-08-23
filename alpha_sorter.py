from sorter import Sorter

class AlphaSorter(Sorter):
	""" child class for alphabetic sorting operations on lists

	Attributes:
		inherited from parent Sorter
	"""	
	def __init__(self, data, sort_order):
		super().__init__(data, sort_order)

	def data_trim_nums(self, input_data):
		""" remove non-alphabetic values from each list

		Args:
			input_data (list of lists): self.data, list of lists of strings
		Return:
			list of lists: each list will only have alphabetic values remaining 
		"""
		output_data = []
		for row in input_data:
			output_row = []
			for el in row:
				if not self.is_float(el) and not self.is_int(el):
					output_row.append(el)
			output_data.append(output_row)
		
		return output_data

	def sort_on_str(self, x):
		""" key to define the sorting rules, sort on pure string values
		"""
		return x.replace("'",'')

	def sort(self):
		"""
		Return:
			list of strings: each string is the output string and each list is the row in csv
		"""
		new_data = self.data_trim_nums(self.data)
		sorted_data = [sorted(row, key=self.sort_on_str, reverse=self.reversed) for row in new_data] # sort each list of alpha values
		result = [', '.join(row) for row in sorted_data] # combine alpha values into a single string per list
		
		return result