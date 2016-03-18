""" This module is intended to be used with file_parse.py
    This is an example intended to show how to do basic parsing.
    The example prints the number of the column followed by the content of the field
"""
out_string = "" # global variable used to encapsulate what will be written to the out file
""" This function deals with the array split by the delimiter it is called as many times as there are lines in the file
"""
def do_with_delimiter_array(array):
    for i in range(0,len(array)):
        do_with_delimiter_field(array[i],i,array)
""" This function is auxiliary to deal with field logic
"""

def do_with_delimiter_field(field,column,array):
    global out_string
    #out_string = out_string +str(column)+':'+str(field)+'\n'
    out_string = out_string +str(field)+'|'
