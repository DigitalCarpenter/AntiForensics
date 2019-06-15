import os
from os import walk
import hashlib
from shutil import copy2

#constants
 
tool_directory = '' #<-here you have to hardcode your analysis-tools-directory.


#funktionen
def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

#main
os.chdir(tool_directory)

#read directory with tools
f = []
for (dirpath, dirnames, filenames) in walk(tool_directory):
    f.extend(filenames)
    break

print ("filename \tMD5 \t\t\t\t\t\t\t\tRenamed to \t\t\t\t\t\t\t\tNew-MD5")

try:
    for elem in f:
        #generate MD5-Sum
        hash = md5(elem)
        #duplicate file
        outfile = hash+'.exe'
        copy2(elem,outfile)
        file = open(outfile, 'a')
        file.write(hash)
        file.close()
        new_hash = md5(outfile)
        print (str(elem) + '\t' + str(hash) + '\t' + str(outfile) + '\t' + str(new_hash))

except:
        print ("There was an error. Perhaps there are old renamed files in the directory?")


