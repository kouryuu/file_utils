# Program to do file juggling
import sys
import delimiter_definitions as dd
in_file = open(sys.argv[1])
in_file_str = in_file.read()
in_file_array = in_file_str.split()
delimiter = '|'
out_file = open(sys.argv[2])


for i in range(0,len(in_file_array)):
    delimiter_separated = in_file_array[i].split(delimiter)
    dd.do_with_delimiter_array(delimiter_separated)


