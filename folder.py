import os, csv
import shutil


with open("new_names.csv") as new:
    new_write = csv.reader(new, delimiter='\n',quotechar='"')
    
    for i in new_write:
        first_folder=r"C:\\Users\Admin\Desktop\\Folder Creator\\mjm\\test\\" + str(i[0])
        client_details1=r"C:\\Users\Admin\Desktop\\Folder Creator\\mjm\\test\\" + str(i[0]) +"\\Client Details"
        Downloads=r"C:\\Users\Admin\Desktop\\Folder Creator\\mjm\\test\\" + str(i[0]) +"\\Downloads"
        Workings=r"C:\\Users\Admin\Desktop\\Folder Creator\\mjm\\test\\" + str(i[0]) +"\\Workings"
        try:
            a= "-".join(i)
            os.makedirs(Downloads,mode = 0o777)
            os.makedirs(Workings,mode = 0o777)
            shutil.copy2("C:\\Users\\Admin\\Desktop\\Folder Creator\\mjm\\Client Name-Client ID\\Client ID-Name-GSTR-3B-2020-10.xlsx",first_folder)
            renamer_path=first_folder+"\\Client ID-Name-GSTR-3B-2020-10.xlsx"
            print(i)
            reverse_rename= (str(i[0]).split("-"))
            reverse_rename.reverse()
            reverse_rename1="-".join(reverse_rename)
            renamed_path=first_folder+"\\"+reverse_rename1+"-GSTR-3B-2020-10.xlsx"
            print(reverse_rename1)
            os.rename(renamer_path,renamed_path)    
        except:
            pass
    # new_write.writerow([str(i)])  