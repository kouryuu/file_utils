"""" Program to do file parsing
    made by Rodrigo R
    it depends on delimiter_definitions to define the row-based and the field based operations

"""
import sys # to read argv from command line
import delimiter_definitions as dd #You should define your own delimiter definitions.
if( sys.argv[1] == sys.argv[2]): #Self output
    in_file = open(sys.argv[1],'r+b')
    in_file_str = in_file.read()
    in_file_array = in_file_str.split()
    out_file = in_file
else:
    in_file = open(sys.argv[1],'r')
    in_file_str = in_file.read()
    in_file_array = in_file_str.split()

delimiter = ',' #should this be hardcoded?
out_file = open(sys.argv[2],'w') #should I create it if it does not exist?


for i in range(0,len(in_file_array)):
    delimiter_separated = in_file_array[i].split(delimiter)
    dd.do_with_delimiter_array(delimiter_separated)
print dd.out_string
out_file.write(dd.out_string)
in_file.close()
out_file.close()
