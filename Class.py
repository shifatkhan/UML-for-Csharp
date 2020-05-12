# CLASS: Containor class for the classes we find. Hold data about their
# variables and methods.
class Class:
    def __init__(self, name):
        self.name = name
        self.parents = list()
        self.variables = dict()
        self.methods = dict()

    def __str__(self):
        str = "Class name: " + self.name + "\n"
        str += "Parents: "
        for p in self.parents:
            str += p + ", "
        str += "\n"
        return str
