# # My goal is write in a specific file asps who not exist there. 
import os
import re

# paths and files to read/ write
directory = "C:\\Users\\ramons\\Desktop\\teste2"
file_to_read = "C:\\Users\\ramons\\Desktop\\teste2\\sou-a-lista.txt"
file_to_write = "C:\\Users\\ramons\\Desktop\\teste2\\zuados.txt"
cs_to_search = "C:\\Users\\ramons\\Desktop\\teste2\\TZDB.inc"

lines = open(file_to_read, 'r').readlines() 

with open(file_to_write, "a") as file_to_write:
    for cs in lines:
        if not cs.replace("\n", "") in open(cs_to_search, encoding="ANSI").read():
            print("nao achei o %s ", cs)