try:
  raise Exception("borked!")

except Exception as e:
  print(e)
