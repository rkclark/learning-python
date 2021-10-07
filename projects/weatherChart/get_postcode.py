import re

postcode_regex = r"^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$"


def get_postcode():
  while True:
    postcode = input("Enter postcode:\n")

    match = re.search(postcode_regex, postcode)

    if match is not None:
      return postcode

    print("Postcode invalid - please enter a valid one.")
