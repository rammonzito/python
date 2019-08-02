# My goal is write in a specific file asps who not exist there. 

import os
import re

# paths and files to read/ write
diretory = # change the repository
file_to_read = # file to write

# text prefix
prefix = "$fileList[] = '"
sufix = "';\n"

# strings to search
cs_to_search = os.listdir(diretory)

# but first take a selfie
lines = open(file_to_read, 'r').readlines() 
del lines[-1] 
open(file_to_read, 'w').writelines(lines)

#writing file's name
with open(file_to_read, "a") as file_to_write:
    file_to_write.writelines("//Forgotten by time\n")
    for cs in cs_to_search:
        file_cs_to_read = diretory + "\\" + cs
        if ".cs" in cs and "myTrad." in open(file_cs_to_read, encoding="ANSI").read():
            if not cs in open(file_to_read).read():
                file_to_write.write(prefix + cs + sufix)
    file_to_write.write("\n?>")

file_to_write.close()