# Python Modules

"""What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application."""

"""Create a Module
To create a module just save the code you want in a file with the file extension .py:"""

"""ExampleGet your own Python Server
Save this code in a file named mymodule.py"""


"""Use a Module
Now we can use the module we just created, by using the import statement:"""


from mymodule import person2
import platform
import mymodule as mx
import mymodule
mymodule.greeating("Marcel")


mymodule.toodo("17:00")


"""Note: When using a function from a module, use the syntax: module_name.function_name."""

"""Example
Save this code in the file mymodule.py"""

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }


"""Example
Import the module named mymodule, and access the person1 dictionary:"""


a = mymodule.person1["age"]
print(a)

"""Naming a Module
You can name the module file whatever you like, but it must have the file extension .py"""

"""Example
Create an alias for mymodule called mx:"""


a = mx.person1["age"]
print(a)

"""Built-in Modules
There are several built-in modules in Python, which you can import whenever you like."""

x = platform.system()
print(x)

"""Note: The dir() function can be used on all modules, also the ones you create yourself."""

"""Import From Module
You can choose to import only parts from a module, by using the from keyword."""
"""Example
Import only the person1 dictionary from the module:"""


print(person2["age"])


"""Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]"""
