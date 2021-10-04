# pickling is object serialisation/deserialisation

import pickle

example_dict = {1: "one", 2: "two", 3: "three"}

# write to a byte stream
pickle_out = open("example_dict", "wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

# read and deserialise bytestream
pickle_in = open("example_dict", "rb")
imported_dict = pickle.load(pickle_in)

print(example_dict)
print(imported_dict)
