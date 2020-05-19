import re
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('my number is 388-325-2004')
print(mo.group(1) + '\n'+ mo.group(2))
 
