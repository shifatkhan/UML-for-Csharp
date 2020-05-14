# UML-for-Csharp
This is a python code that will turn Unity C# code into a simple UML diagram.
Emphasis on "simple" because it only scrapes the code for:
1. The class name
2. The class's parents
3. Variables
4. Methods

# Note
This will not work with all C# code. It was made in a very "hack" style.
In other words, this is not an actual code interpreter. Your C# code needs the following general structure to make this work:

1. All class variable must be declared before any methods.
2. Variable names should start with lower case letter
3. Method names should start with a CAPITAL letter
4. File names should be the same as the class name declared inside said file (meaning each file has only 1 class)
5. Comments should occupy a line alone without any code. In other words, a line containing code should not contain comments before it
    Example of a wrong code line: /* This is a comment */ public Vector3 thisIsAVariable;

I know this is ugly and spaghetti coding, but it was made for fun :)
Maybe I'll revisit this and remake it using proper C# interpreter
