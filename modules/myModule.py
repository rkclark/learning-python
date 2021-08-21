def hello():
  print('hello')

# will run whenever this module is imported elsewhere
print('module being initialised')

# use this if statement to enclose code that should not be run
# when this file is imported into another file
if __name__ == '__main__':
  print('will only print if we are running this file directly and not when it is imported elsewhere!')