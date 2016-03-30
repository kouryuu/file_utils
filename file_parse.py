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
        try:
            in_file = open(sys.argv[1],'r+b')
        except IOError:
            print "Could not open file: "+str(sys.argv[1])
            raise
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
        try:
            out_file = open(sys.argv[2],'w')
        except IOError:
            print "Could not open file: "+str(sys.argv[2])
            raise

    for i in range(0,len(in_file_array)):
        if(delimiter == False): #in case we just want to return the whole line
            delimiter_separated = in_file_array[i]
        else:
            delimiter_separated = in_file_array[i].split(delimiter)
        dd.do_with_delimiter_array(delimiter_separated)
    print dd.out_string # should it always print to the stdout? or should it only do it when specified stdout?
    if(sys.argv[2] != 'stdout'):
        out_file.write(dd.out_string)
        out_file.close()
    in_file.close()
