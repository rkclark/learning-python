text = 'Sample text to save to a file\nWith a new line!'

targetFile = open('./temp/writeToHere.txt', 'w') # 'w' to write
targetFile.write(text)
targetFile.close()

textToAppend = '\nThis line will be appended to existing file!'

targetFile = open('./temp/writeToHere.txt', 'a') # 'a' to append
targetFile.write(textToAppend)
targetFile.close()

# read file into single string
fileAsString = open('./temp/writeToHere.txt', 'r').read() # 'r' to read
print(fileAsString)

# read each line in file to element in array
fileAsArray = open('./temp/writeToHere.txt', 'r').readlines() # 'r' to read
print(fileAsArray)
