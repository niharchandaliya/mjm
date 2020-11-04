import os, csv
import shutil
with open("new.csv") as new:
    new_write = csv.reader(new, delimiter=',',quotechar='"')
    i=1
    for i in new_write:
        print(i)
        stuff="/home/nickjo/Desktop/code/office_stuff/" + str(i[0])+"/sub1/sub2/"
        try:
            print(stuff)
            os.makedirs(stuff,mode = 0o777)
            shutil.copy2("/home/nickjo/Desktop/code/office_stuff/new.csv",stuff)
        except:
            pass
        
        # new_write.writerow([str(i)])  