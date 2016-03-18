def do_with_delimiter_array(array):
    for i in range(0,len(array)):
        do_with_delimiter_field(array[i],i,array)

def do_with_delimiter_field(field,column,array):
    print str(column) + " . "+str(field)


