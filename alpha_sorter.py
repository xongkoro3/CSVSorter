from sorter import Sorter

class AlphaSorter(Sorter):
	def __init__(self, data, sort_order):
		super().__init__(data, sort_order)

	def data_trim_nums(self, input_data):
		output_data = []
		for row in input_data:
			output_row = []
			for el in row:
				if not self.is_float(el) and not self.is_int(el):
					output_row.append(el)
			output_data.append(output_row)
		
		return output_data

	def sort_on_str(self, x):
		return x.replace("'",'')

	def sort(self):
		new_data = self.data_trim_nums(self.data)
		sorted_data = [sorted(row, key=self.sort_on_str, reverse=self.reversed) for row in new_data]
		result = [', '.join(row) for row in sorted_data]
		
		return result