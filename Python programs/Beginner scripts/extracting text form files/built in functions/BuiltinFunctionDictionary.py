

#Append the content of the txt file to fulltext
fulltext=[]
opDoc=open('BuiltinFunctions.txt', 'r', encoding='latin1')
fulltext=opDoc.read()
#print('Appended content to fulltext\n')


import re
#find function
function_regex=re.compile( r'(?<=Python\s)(.*?)(?=\(\)\n)')
functions= function_regex.findall(fulltext)
#print('Functions extracted from fulltext \n ')


#find description
descriptions=re.findall(r'Python\s+[^()]+\(\)\n(.*)\n', fulltext)
#print('Descriptions extracted from fulltext \n ')


dic={}

for function in functions:
    dic[function]= ''
print('Assigned functions values to the dictionary.\n')



i=0
for function in functions:
    dic[function]= descriptions[i]
    i=i+1
print('Assigned desctiption values to the dictionary.\n')


import pickle
pickle_out = open("dict.pickle","wb")
pickle.dump(dic, pickle_out)
pickle_out.close()

def a():
    query=input()
    if query in functions:
        print(str(dic[query]))
        print('\n\nWhich built-in function would you like to check?')
        a()
    if query not in functions:
        print('No function with this name')
        print('\n\nWhich built-in function would you like to check?')
        a()
print('Which built-in function would you like to check?')
a()


