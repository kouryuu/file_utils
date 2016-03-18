global out_string 

def do_with_delimiter_array(array):
    for i in range(0,len(array)):
        do_with_delimiter_field(array[i],i,array)

def do_with_delimiter_field(field,column,array):
    out_string = out_string + str(field) + "-" 


