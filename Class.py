# CLASS: Containor class for the classes we find. Hold data about their
# variables and methods.
class Class:
    def __init__(self, name):
        self.name = name
        self.parents = list()
        self.variables = list()
        self.methods = list()

    def __str__(self):
        str = "Class name: " + self.name + "\n"
        str += "Parents: "
        for p in self.parents:
            str += p + ", "
        str += "\n"
        str += "Variables: "
        for v in self.variables:
            if v.access != "":
                str += v.access + " "
            str += v.type + " " + v.name + ", "
        str += "\n"
        str += "Methods: "
        for m in self.methods:
            if m.access != "":
                str += m.access + " "
            str += m.returntype + " " + m.name + "("
            for p in m.params:
                str += p.name + ", "
            str += "), "
        str += "\n"
        return str

class Variable:
    def __init__(self, name):
        self.name = name
        self.type = ""
        self.access = ""

    @classmethod
    def full_init(self, name, type, access):
        self.name = name
        self.type = type
        self.access = access

    def __str__(self):
        str = ""
        if self.access != "":
            str += self.access + " "
        str += self.type + " " + self.name
        return str

class Method:
    def __init__(self, name):
        self.name = name
        self.returntype = ""
        self.access = ""
        self.params = list()

    def __str__(self):
        str = ""
        if self.access != "":
            str += self.access + " "
        str += self.returntype + " " + self.name + "("
        for p in self.params:
            str += p + ", "
        str += ")"
        return str
