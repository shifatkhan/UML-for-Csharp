# A python program that creates UML diagrams from C# scripts.
# @author Shifat Khan

from pathlib import Path
from Class import Class, Variable, Method

# FUNCTION: Gets all C# files in given directory.
def get_classes(dir):
    # Find all C# files in directory (including subdirectories)
    file_list = Path(dir).glob('**/*.cs')
    classes = dict()

    for file_path in file_list:
        class_name = file_path.parts[len(file_path.parts) -1]
        temp_class = Class(class_name)
        get_class_details(str(file_path), temp_class)
        classes[class_name] = temp_class

    return classes

# FUNCTION: Gets all parents, variables and methods of a certain class file.
def get_class_details(dir, class_obj):
    file_path = Path(dir)

    print ("@Debug: Processing file "+file_path.parts[len(file_path.parts) -1])

    with file_path.open() as file_text: # Open said file.
        searching_var = False # Bool for when we're searching for variables.
        inside_class = False # Bool that keeps status of whether we're in the class or not.

        for line in file_text: # Read each line.
            words = line.split() # All words in one line.

            # Skip comments and import code.
            if words and (words[0] != "using" and not words[0].startswith("//") and not words[0].startswith("/*") and not words[0].startswith("*") and not words[0].startswith("*/")):
                for i in range(0, len(words)):
                    print("@Debug: \tprocessing word " + words[i])

                    # Find inheritance
                    if words[i] == "class":
                        print("@Debug: \t\tIS CLASS " + words[i+1])
                        if i+3 <= len(words)-1:
                            for j in range(i+3, len(words)): # Get ALL parent classes.
                                print("@Debug: \t\t\tIS PARENT " + words[j].replace(",", ""))
                                class_obj.parents.append(words[j].replace(",", ""))
                        break # Need to break since i's value gets reset

                    # Find class variables that are Objects
                    elif words[i][0].isupper():
                        print("@Debug: \t\tIS UPPER " + words[i])
                        if i-1 >= 0:
                            if words[i-1] == "public" or words[i-1] == "private" or words[i-1] == "protected":
                                temp_var = Variable(words[i+1].replace(";", ""))
                                temp_var.type = words[i]
                                if i-1 >=0:
                                    temp_var.access = words[i-1]
                                else:
                                    temp_var.access = "protected"
                                class_obj.variables.append(temp_var)
                            elif words[i-1] != "new":
                                temp_method = Method(words[i].split("(")[0]) # Method name
                                temp_method.returntype = words[i-1] # Method return type
                                if i-2 >= 0:
                                    temp_method.access = words[i-2] # Methods access modifier
                                else:
                                    temp_method.access = "protected"
                                j = i+1
                                while j < len(words):
                                    if words[j] != ":":
                                        temp_method.params.append(Variable(words[j].replace(",","")))
                                    j += 1
                                class_obj.methods.append(temp_method)

                    # Find first opening bracket to state that we're inside the class
                    if not searching_var and not inside_class and words[i].find("{") != -1:
                        searching_var = True
                        inside_class = True
                        print("@Debug: \t\tSTART VAR SEARCH " + words[i])

                    # Once inside the class, look for all variables.
                    elif searching_var:
                        print("",end="")
                        if words[i].find("{") != -1: # If we find an Opening bracket
                            searching_var = False
                            print("@Debug: \t\tEND VAR SEARCH " + words[i])
                        else:
                            # Check if word is a datatype
                            if i+1 < len(words) and not words[i][0].isupper() and words[i] != "public" and words[i] != "private" and words[i] != "protected":
                                if words[i].find("(") == -1 and words[i+1].find("(") == -1: # Check if it's not something else
                                    print("@Debug: \t\tFOUND VAR " + words[i+1])
                                    temp_var = Variable(words[i+1].replace(";", ""))
                                    temp_var.type = words[i]
                                    if i-1 >=0:
                                        temp_var.access = words[i-1]
                                    else:
                                        temp_var.access = "protected"
                                    class_obj.variables.append(temp_var)
                                break
        inside_class = False
    print ("\n")


# TESTING------------------------------------------------------------------
classes = get_classes('./TestCsharpProject')

print("\nTEST OUTPUT:")
for x, y in classes.items():
    print(y)
