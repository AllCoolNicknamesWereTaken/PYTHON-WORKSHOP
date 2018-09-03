import os
import pickle
path = os.path.join(".", "example")
# simple_file = file(path, "w")
# simple_file.write("""zdradzona
#     jak nigdy""")

somefile = file(path, "r")

print somefile.readline()
print somefile.readline()

# del simple_file
del somefile

simple_file = file("test.pickle", "w")
important_data = ("cos", 6, 15.6)
pickle.dump(important_data, simple_file)
del simple_file
