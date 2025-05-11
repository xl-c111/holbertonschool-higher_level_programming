#!/usr/bin/python3
"""
import os to import built-in os mudule, which provides a way to interact with operating system 
os.write(): send output directly to the terminal
os.write(fd, data): argument 1 - file descriptor for standard output (stdout)
                                 0 = standard input
                                 1 = standard output
                                 2 = standard error
                    argument 2: b"#pythoniscool\n"
                                prefix b: means this is a bytes literal
                                "#pythoniscool\n" is the message followed by a newline character
"""
import os
os.write(1, b"#pythoniscool\n")

# another solution
# __import__('os').write(1, b"#pythoniscool\n")

"""
difference between import and __import__
import: statement
e.g., import math
      print(math.sqrt(9))
__import__: built-in function 
e.g., mod = __import__('math')     # you can importa module as a string 
      print(mod.sqrt(9))
"""
