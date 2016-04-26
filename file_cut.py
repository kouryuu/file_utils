#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""" Program to do file parsing
    made by Rodrigo R <https://github.com/kouryuu/>
    it depends on delimiter_definitions to define the row-based and the field based operations

"""

import sys # to read argv from command line
import subprocess #This allows to call wc on *nix systems

if(len(sys.argv) <= 2): #Too few arguments protection
    print '''You need to specify both in the command line the arguments
file_cut [file] [pieces]
'''
    sys.exit()
else:
    file_name = str(sys.argv[1])
    pieces = int(str(sys.argv[2]))
    if(pieces == 0):
        raise Exception("The second argument cannot be zero.")
    if(pieces == 1):
        raise Exception("Very funny, just cut it yourself in one piece.")
    try:
        in_file = open(file_name,'r+b')
    except IOError:
        raise Exception("Could not open file: "+file_name)
    print 'Counting the number of lines in the file'
    lines = int(subprocess.check_output(['wc','-l'],stdin=in_file))
    in_file.close()
    in_file = open(file_name,'r+b')
    piece_size = lines / pieces
    if(piece_size == 0):
        raise Exception("There are too many pieces, you should specify a smaller number than "+str(lines))
    for i in range(1,pieces+1):
        seq_filename = file_name+'.p'+str(i)
        out_file = open(seq_filename,'w')
        for j in range(1,(piece_size)):
            if lines != 0:
                line_contents = in_file.readline()
                out_file.write(line_contents)
        print "File "+str(i)+" of "+str(pieces)+" written. "+seq_filename
        out_file.close()
    print "Done."
