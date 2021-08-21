def myFunction(arg1, arg2):
  print('This is my function', arg1, arg2)

myFunction('hello', 'world')

def addNumbers(a = 1, b = 1):
  print(a+b)
  return a+b

addNumbers(); # 2

addNumbers(b=5, a=2) #7