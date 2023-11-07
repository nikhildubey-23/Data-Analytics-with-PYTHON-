import shutil as sh
import os as os
file_name = input("enter the name of your file\n")
method = input("enter the method you want to use for read enter r , for write enter w and for editing enter a\n")
#first we use the open function to open a file
file = open(file_name, f"{method}")
if method == "w":
    file.write(input("enter the text you want to write in the file\n"))
elif method == "r":
    print(file.read())
elif method == "a":
    file.write(input("enter the text you want to add in the file\n"))
else:
    print("invalid method")
file.close()
# now we will use the shutil module to copy the file
sh.copy(file_name, "copy.txt")
# now we will use the os module to rename the file
os.rename(file_name, "new_file.txt")
# now we will use the os module to delete the file
os.remove("new_file.txt")
