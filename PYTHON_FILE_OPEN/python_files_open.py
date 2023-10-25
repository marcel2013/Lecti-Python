"""File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

"""

"""File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:"""

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists"""

# In addition you can specify if the file should be handled as binary or text mode

"""
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)"""

# f = open("New Text Document.txt", "r")
# print(f.read())


# print("Current Directory:", os.getcwd())

"""Open a File on the Server
Assume we have the following file, located in the same folder as Python:"""

# f = open("demofile.txt", "r")
# print(f.read())

"""If the file is located in a different location, you will have to specify the file path, like this:"""

"""Example
Open a file on a different location:"""


# f = open("C:\\Users\\user\Desktop\\Adrese Pyton\\adrese python.txt", "r")
# print(f.read())


"""Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return:

Example
Return the 5 first characters of the file:"""

# f = open("demofile.txt", "r")
# print(f.read(10))

"""Read Lines
You can return one line by using the readline() method:"""

# f = open("demofile.txt", "r")
# print(f.readline())

# By calling readline() two times, you can read the two first lines:

# f = open("demofile.txt", "r")
# print(f.readline())
# print(f.readline())

"""By looping through the lines of the file, you can read the whole file, line by line:

Example
Loop through the file line by line:"""

# f = open("demofile.txt", "r")
# for x in f:
import os
 # print(x)

"""Close Files
It is a good practice to always close the file when you are done with it.

Example
Close the file when you are finish with it:"""

f = open("demofile.txt", "r")
print(f.readline())
f.close()

"""Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file."""
