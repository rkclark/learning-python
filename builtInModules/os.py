import os

# get current dir
currentDir = os.getcwd()

print(currentDir)

# make dir

os.mkdir("newDir")

# rename dir

os.rename("newDir", "newDir2")

# delete dir

os.rmdir("newDir2")
