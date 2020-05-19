import os, pprint
folderNames=[]
subFolders=[]
filenames=[]
for folder_names, subfolder_names, file_names in os.walk(r'C:\Users\Patrick\Desktop\Musica'):
    try:
        folderNames.append(folder_names)
        openFolderNames=open('allFolders.txt', 'w', encoding='utf-8')
        openFolderNames.write('\n'.join(folderNames))
        
    except UnicodeEncodeError:
        errorTxt=open('errorsfolder.txt', 'w', encoding='utf-8')
        errorTxt.write('Foldernames error - It was not possible to code this file.')
        errorTxt.close()
    
    for subfolder_name in subfolder_names:
        subFolders.append(subfolder_name)
        opensubfolders=open('allSubfolders.txt', 'w', encoding='utf-8')
        opensubfolders.write('\n'.join(subFolders))
        
    for file_name in file_names:
        try:
            import pprint
            filenames.append(file_name)
            openfilenames=open('allfilenames.txt','w', encoding='utf-8')
            openfilenames.write('\n'.join(filenames))
            
        except UnicodeEncodeError:
            errorTxt=open('errorsfile.txt', 'w')
            errorTxt.write('filenames error - It was not possible to code this file.')
            errorTxt.close()       
            
print('Done!!!')



