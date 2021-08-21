x = 6

def printX():
  global x
  x+=5 # can only do this if x is set to global, otherwise get error
  print(x)

printX()