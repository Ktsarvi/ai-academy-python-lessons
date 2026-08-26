class TextEditor:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def write(self, text):
        with open(self.file_name, self.mode) as f:
            return f.write(text)

    def read(self):
        with open(self.file_name, "r") as f:
            return f.read()

    def append(self, text):
        with open(self.file_name, "a") as f:
            return f.write(text)

myeditor = TextEditor("example1.txt", "w")

myeditor.write("Hello\n")
myeditor.append("World")
print(myeditor.read())