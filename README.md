# I wanted to do AWK stuff with Python

This repo is intended to have a set of file utilities used to manipulate files using Python.
Normally I would use *AWK* but I think Python could manage many fancy things and make it more readable and modern.

## Utilities so far
- file_parse

### File parse
Usage `file_parse [in-file] [out-file] (optional)[delimiter]` .
You should define your own `delimiter_definitions.py` or override the `do_with_delimiter_array()` function that receives the array of each line split by the delimiter.
