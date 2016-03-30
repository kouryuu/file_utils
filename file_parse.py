#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""" Program to do file parsing
    made by Rodrigo R <https://github.com/kouryuu/>
    it depends on delimiter_definitions to define the row-based and the field based operations

"""

import sys # to read argv from command line
import delimiter_definitions as dd #You should define your own delimiter definitions.

if(len(sys.argv) <= 2): #Too few arguments protection
    print '''You need to specify both in the command line the arguments
file_parse [in-file] [out-file] (optional)[delimiter]
If instead of out-file you specify stdout it will output it to stdout'''
    sys.exit()
else:
    if( sys.argv[1] == sys.argv[2]): #Self output
        in_file = open(sys.argv[1],'r+b')
        in_file_str = in_file.read()
        in_file_array = in_file_str.split('\n')
        out_file = in_file
    else:
        in_file = open(sys.argv[1],'r')
        in_file_str = in_file.read()
        in_file_array = in_file_str.split('\n')
    if(len(sys.argv) == 3): #optionaly give the delimiter
        delimiter = dd.delimiter
    else:
        delimiter = sys.argv[3]
    if(sys.argv[2] != 'stdout'):
        out_file = open(sys.argv[2],'w') #should I create it if it does not exist?

    for i in range(0,len(in_file_array)):
        delimiter_separated = in_file_array[i].split(delimiter)
        dd.do_with_delimiter_array(delimiter_separated)
    print dd.out_string
    if(sys.argv[2] != 'stdout'):
        out_file.write(dd.out_string)
        out_file.close()
    in_file.close()
    
