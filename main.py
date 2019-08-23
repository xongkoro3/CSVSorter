import csv
import sys
import os.path
from os import path
from num_sorter import NumSorter
from alpha_sorter import AlphaSorter


def input_params_valid(name, sort_type, sort_order):
	acceptable_sort_types = ['numeric', 'alpha', 'both']
	acceptable_sort_orders = ['ascending', 'descending']

	if (not name.endswith('.csv')):
		print ("Sorting is currently only supported on csv files")
		return False
	if (not path.exists(name)):
		print ("File does not exist")
		return False
	if (sort_type not in acceptable_sort_types):
		print ("Acceptable sorting types are: " + str([i for i in acceptable_sort_types]))
		return False
	if (sort_order not in acceptable_sort_orders):
		print ("Acceptable sorting orders are: " + str([i for i in acceptable_sort_orders]))
		return False
	
	return True

def read_csv_to_list(file_name):
	""" read csv file into processable data
		Return:
			list of list of strings: each list has string values in that row
	"""
	with open(file_name, 'r') as f:
		data = [[x.lstrip() for x in line] for line in csv.reader(f)]
	return data


def main():
	if (len(sys.argv) != 4):
		print ("Invalid number of input params")
		return 

	if (input_params_valid(sys.argv[1], sys.argv[2], sys.argv[3])):
		""" Check if the params are valid and set the params accordingly
		"""
		FILE_NAME = sys.argv[1]
		SORT_TYPE = sys.argv[2]
		SORT_ORDER = sys.argv[3]
		
		data = read_csv_to_list(FILE_NAME)

		if (SORT_TYPE == 'numeric'):
			s = NumSorter(data, SORT_ORDER)
			res_list = s.sort()
		elif (SORT_TYPE == 'alpha'):
			s = AlphaSorter(data, SORT_ORDER)
			res_list = s.sort()
		else:
			num = NumSorter(data, SORT_ORDER)
			alpha = AlphaSorter(data, SORT_ORDER)
			num_list = num.sort()
			alpha_list = alpha.sort()

			res_list = [num_list[i] + ', ' + alpha_list[i] for i in range(len(num_list))] # concatenate num result string and alpha result string

		# Print final result to console
		for res_row in res_list:
			print (res_row.lstrip(', ').rstrip(', ')) # removing commmas from joining both

if __name__ == '__main__':
	main()
	