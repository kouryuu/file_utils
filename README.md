# I wanted to do AWK stuff with Python

This repo is intended to have a set of file utilities used to manipulate files using Python.
Normally I would use *AWK* but I think Python could manage many fancy things and make it more readable and modern.

## Utilities so far
- file_parse

### File parse
Usage `file_parse [in-file] [out-file] (optional)[delimiter]` .
You should define your own `delimiter_definitions.py` or override the `do_with_delimiter_array()` function that receives the array of each line split by the delimiter.
Optionally you could output to the standard out by specifying `stdout` instead of the out filename.


#### Examples
Some useful `delimiter_definitions.py` examples are:

** Skip one line **

```python
out_string = "" # global variable used to encapsulate what will be written to the out file
delimiter = False # by specifying False we force file_parse to return the whole line without splitting and making an array based on the delimiter
counter = 0
def do_with_delimiter_array(array):
    global counter
    global out_string
    if(counter % 2):
      out_string += array+'\n'
    counter += 1
```
