import os

directory = "" #change directory
file_to_read = "old_asps.txt"
search = os.listdir(directory)

lines = open(file_to_read, 'r').readlines() 

for l in lines:
    path = os.path.join(directory, l.rstrip('\n')) 
    if (os.path.exists(path)):
        print("removing " + l)
        os.remove(path)