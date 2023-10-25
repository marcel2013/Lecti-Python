"""Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content"""

"""ExampleGet your own Python Server
Open the file "demofile2.txt" and append content to the file:"""

# f = open("demofile2.txt", "a")
# f.write("Now the file has content!")
# f.close()

# open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())


"""Example
Open the file "demofile3.txt" and overwrite the content:"""

# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# open and read the file after the overwriting:

# f = open("demofile3.txt", "r")
# print(f.read())

# Note: the "w" method will overwrite the entire file.

"""Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist"""

# f = open("myfile.txt", "x")

# Result: a new empty file is created!

"""Example
Create a new file if it does not exist:"""

# f = open("myfile.txt", "w")

"""Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:"""

"""ExampleGet your own Python Server
Remove the file "demofile.txt":"""


# os.remove("demofile.txt")


"""Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:"""

"""Example
Check if file exists, then delete it:"""

# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("The file does not exist")

"""Delete Folder
To delete an entire folder, use the os.rmdir() method:"""

"""Example
Remove the folder "myfolder":"""

import os
os.rmdir("myfolder")

# Note: You can only remove empty folders.
