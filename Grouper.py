
import os

cwdir =  os.getcwd()

print("\nCurrent Working Directory : {}\n".format(cwdir))

folder_dirs = os.listdir("{}".format(cwdir))    # Get files name in folder

for i in folder_dirs:   
    a = i.split(".")
    try :
        try:    # Make Folder If not their
            b = "{}\\".format(cwdir)
            path = os.path.join(b,a[-1])
            os.makedirs(path)
            print("Creted : ",a[-1])
        finally:    # replace File Place To Correct Folder
            if a[0] != "Grouper":       
                c_file_place = os.path.join(cwdir,"{}.{}".format(".".join(a[:-1]),a[-1]))
                new_file_place = os.path.join(cwdir,"{}\\{}.{}".format(a[-1],".".join(a[:-1]),a[-1]))
                os.rename(c_file_place,new_file_place)
    except Exception as e:
        pass

input("Press Enter To Continue : ")
