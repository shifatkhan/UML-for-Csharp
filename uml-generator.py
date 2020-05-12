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

pathlist = Path('./TestCsharpProject').glob('**/*.cs')
for path in pathlist:
     # because path is object not string
     path_in_str = str(path)
     print(path.parts[len(path.parts) -1])
