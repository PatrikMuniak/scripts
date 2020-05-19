import re
#find function
fulltext="\rPython classmethod()\rreturns class method for given function\r"
function_regex=re.compile( r'(?<=\rPython)(.*?)(?=\r)')
function= function_regex.findall(fulltext)
print(function)


#find description
fulltext="\rPython classmethod()\rreturns class method for given function\r"
description=re.findall(r'\rPython\s+[^()]+\(\)\r(.*)\r', fulltext)
print(description)


dic={'function':function, 'description':description}


