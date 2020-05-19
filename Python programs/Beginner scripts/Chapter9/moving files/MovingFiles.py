import shutil, os
shutil.copy('fileToMove.txt','copyHere')
#if you copy multiple times, it gets overwritten
shutil.copy('fileToMove.txt','copyHere\\fileToMove2.txt')
for i in range(5):
    shutil.copy('fileToMove.txt','copyHere\\fileToMove'+str(i)+'.txt')
