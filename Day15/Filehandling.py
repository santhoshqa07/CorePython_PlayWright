#Example 1: creating/writing a file
#Approach 1
# file = open("C:\\Automation\\PWpython\\myfile.txt",'w')
# file.write("Welcome to Python \n File handling")
# file.close()

#Approach 2
# with open("C:\\Automation\\PWpython\\myfile.txt",'w') as file:
#     file.write("Welcome to Python \n File handling")
#     file.close()

#Example 2: Appending a file.
# file = open("C:\\Automation\\PWpython\\myfile.txt",'a')
# file.write("\n This is the appended line")
# file.close()

#Example 3: Reading data from text file
#read()- reads entire data
#readline()- read single line
#readlines()- read all the lines in to list format

#Example 3: Reading data from the text file.
# file = open("C:\\Automation\\PWpython\\myfile.txt",'r')
# content = file.readlines()
# print(content)
# file.close()

#Example 4: Renaming the file.
# import os
# os.rename("C:\\Automation\\PWpython\\myfile.txt","C:\\Automation\\PWpython\\myfile1.txt")
# print("File Renamed")

#Example 5: Deleting the file
# import os
# file= ("C:\\Automation\\PWpython\\myfile.txt")
#
# if os.path.exists(file):
#     os.remove(file) 
# else:
#     print("File does'nt exist...")

# #Example 6: Creating a directory/Folder
# import os
# os.mkdir("D:\\New\\New1\\Mydir")
# print(" Directory created")

#Example 7: check the directory exist or not
# import os
# my_dir="D:\\New\\New1\\Mydir"
#
# if os.path.exists(my_dir):
#     print("Directory exists")
# else:
#     print("Directory does not exist")

#Example 8: Rename the directory

# import os
# os.rename("D:\\New\\New1\\Mydir", "D:\\New\\New1\\Mydir1")
# print("Directory renamed")

#Example 9: remove the directory
# import os
# os.rmdir("D:\\New\\New1\\Mydir1") #Deletes only if folder/directory is empty

# import shutil
# shutil.rmtree("D:\\New\\New1\\Mydir1") #Only if the folder or directory contains files

#Example 10: get the current working directory

import os
print(os.getcwd())
























