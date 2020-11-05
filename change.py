import os
import sys
import csv
with open("new_names.txt", mode="w") as new_names:
    writer=csv.writer(new_names)
    with open("Folder.csv", mode="r") as name:
        new_write = csv.reader(name, delimiter=',',quotechar='"')
        for i in new_write:
            new_i=i.reverse()
            
            reverse_list="-".join(i)
            print(reverse_list)
            new_names.write(reverse_list+"\n")    



