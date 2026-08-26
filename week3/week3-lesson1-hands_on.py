import os

# write in file absolute path
with open("example.txt","a+") as f:
    for i in range(2):
          f.write("Appended line %d\r\n" % (i+1))

# write in file relative path
file_path = os.path.join(os.path.dirname(__file__), "example.txt")

with open(file_path, "a+") as f:
    for i in range(2):
        f.write("Appended line %d\r\n" % (i + 1))
