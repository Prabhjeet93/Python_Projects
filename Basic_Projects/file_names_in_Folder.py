import os


# Get the list of directory and files in the current directory.
print(os.listdir())



# Get the list of all files and directories from the particular path
path = "C://Users"
dir_list = os.listdir(path)

print(dir_list)


# To get all the files, and no folders.

path = "C://Users"
files = os.listdir(path)
files = [f for f in files if os.path.isfile(path+'/'+f)] #Filtering only the files.
print(*files, sep="\n")



# To get only particular file. Foreexample .txt or .pdf files.

for x in os.listdir():
    if x.endswith(".txt"):
        print(x)


# OS.walk() generates file names in a directory tree. This function returns a list of files in a tree structure. 
# The method loops through all of the directories in a tree.

# Return: returns the name of every file and folder within a directory and any of its subdirectories.


path = "C://Users//tt//github"
 
# to store files in a list
list = []
 
# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        print(f)
        if '.txt' in f:
            print(f)

