# # A python program that creates UML diagrams from C# scripts.
#
#
# class Robot:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#
#     def introduce_self(self):
#         print("My name is " + self.name + ", beep boop.")
#
# class Person:
#     def __init__(self, name, personality, is_sitting):
#         self.name = name
#         self.personality = personality
#         self.is_sitting = is_sitting
#
#     def sit_down(self):
#         self.is_sitting = True
#
#     def stand_up(self):
#         self.is_sitting = False
#
# r1 = Robot("Tom", "blue", 30)
# r2 = Robot("Jerry", "brown", 10)
#
# p1 = Person("Alice", "aggressive", False)
# p2 = Person("Becky", "talkative", True)
#
# # Person owns robots
# p1.robot_owned = r2
# p2.robot_owned = r1
#
# p1.robot_owned.introduce_self()
#
# e1 = [x ** 2 for x in range(6, 0, -1)]
# print(e1)
#
# # Dictionary
# d = {}
# d["speed"] = r1
#
# print(d["speed"].name)

from pathlib import Path

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

# FUNCTION: Gets all C# files in given directory.
def get_class_information(dir):
    # Find all C# files in directory (including subdirectories)
    file_list = Path(dir).glob('**/*.cs')
    classes = dict()

    for file_path in file_list:
        class_name = file_path.parts[len(file_path.parts) -1]
        temp_class = Class(class_name)
        get_class_variables(str(file_path), temp_class)
        classes[class_name] = temp_class

    return classes

# FUNCTION: Gets all variables of a certain class file.
def get_class_variables(dir, class_obj):
    file_path = Path(dir)

    print ("@Debug: Processing file "+file_path.parts[len(file_path.parts) -1])

    with file_path.open() as file_text: # Open said file.
        for line in file_text: # Read each line.
            words = line.split() # All words in one line.

            # Skip comments and import code.
            if words and (words[0] != "using" and not words[0].startswith("//") and not words[0].startswith("/*") and not words[0].startswith("*") and not words[0].startswith("*/")):
                for i in range(0, len(words)):

                    # Find inheritance
                    if words[i] == "class":
                        if i+3 <= len(words)-1:
                            for j in range(i+3, len(words)): # Get ALL parent classes.
                                class_obj.parents.append(words[j].replace(",",""))
                        break
                #     else:
                #         print(words[i], end = ' ')
                # print()

# TESTING------------------------------------------------------------------
classes = get_class_information('./TestCsharpProject')

c1 = Class("Person")

print("Classes dict:")
for x, y in classes.items():
    print(y)
