#1. Exploring Python's OS Module
#Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

#Task 1: Directory Inspector:

#Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

import os

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
    try:
        print(f"\n\033[7m{path}:\033[0m")
        for object in os.listdir(path):
            fullpath = os.path.join(path,object)
            if os.path.isdir(fullpath):
                list_subdir(fullpath,1)
            else:
                print(object)
    except FileNotFoundError:
        print("\n\033[7mThat directory does not exist, please try again\033[0m")
    except PermissionError:
        print("\n\033[7mYou do not currently have permission to access this directory\033[0m")
    except IOError:
        print("\n\033[7mAn unexpected IOError has occurred\033[0m")
    except:
        print("\n\033[7mAn unexpected error has occurred\033[0m")

while True:
    print("\nDirectory Inspector - List all files and subdirectories of a directory")
    print("1: Inspect the provided test directory")
    print("2: Provide your own directory to Inspect")
    print("3: Exit")
    choice = input("Which function would you like to execute?: ")

    if choice == '1':
        list_directory_contents("Test_Directory")
    elif choice == '2':
        user_dir = input("What is the full path to the directory you'd like to Inspect?: ")
        list_directory_contents(user_dir)
    elif choice == '3':
        break
    else:
        print("\033[7mThat was not a valid choice, please try again\033[0m")