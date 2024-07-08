#1. Exploring Python's OS Module
#Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

#Task 1: Directory Inspector:

#Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

import os
import re

def list_subdir(path, counter):
    tabs = "\t" * counter
    print(f"\033[7m{tabs}{path}:\033[0m")
    for object in os.listdir(path):
        fullpath = os.path.join(path,object)
        if os.path.isdir(fullpath):
            new_count = counter + 1
            list_subdir(fullpath, new_count)
        else:
            print(f"{tabs}{object}")

def list_directory_contents(path):
    print(f"\033[7m{path}:\033[0m")
    try:
        for object in os.listdir(path):
            fullpath = os.path.join(path,object)
            if os.path.isdir(fullpath):
                list_subdir(fullpath,1)
            else:
                print(object)
    except FileNotFoundError:
        print("That directory does not exist, please try again")
    except PermissionError:
        print("You do not currently have permission to access this directory")
    except:
        print("An unexpected error has occurred")
list_directory_contents("Test_Directory")