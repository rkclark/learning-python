import re

while True:
  postCode = input("Enter postcode:\n")

  postCodeRegex = r"^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$"

  match = re.search(postCodeRegex, postCode)

  if match is not None:
    break

  print("Postcode invalid - please enter a valid one.")
