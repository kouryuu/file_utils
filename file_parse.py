"""" Program to do file juggling
    made by Rodrigo R
    it depends on delimiter_definitions to define the row-based and the field based operations

"""
import sys # to read argv from command line
import delimiter_definitions as dd

in_file = open(sys.argv[1])
in_file_str = in_file.read()
in_file_array = in_file_str.split()

delimiter = '|' #should this be hardcoded?
out_file = open(sys.argv[2]) #should I create it if it does not exist?


for i in range(0,len(in_file_array)):
    delimiter_separated = in_file_array[i].split(delimiter)
    dd.do_with_delimiter_array(delimiter_separated)


