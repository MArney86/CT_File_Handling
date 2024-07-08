#1. Exploring Python's OS Module
#Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

#Task 1: Directory Inspector:

#Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

import os

def list_subdir(path, counter): #a function to "walk" through and print files and subdirectories within the given path and keep count of how deep things are in the tree
    tabs = "\t" * counter #set tabs for output formatting
    
    print(f"\033[7m{tabs}{path}:\033[0m") #print the directory path in a formatted and very visible way
    
    for object in os.listdir(path): #iterate through the objects given by listing the given directory
        fullpath = os.path.join(path,object) #add the current item to the current path to give a testable full path
        if os.path.isdir(fullpath): #check if the current item is a subdirectory
            new_count = counter + 1 #update the counter to show how deep in the file structure the directory is
            list_subdir(fullpath, new_count) #run the list_subdir() function for the new subdirectory
        else: #not a directory
            print(f"{tabs}{object}") #print the current item filename without the rest of the path

def list_directory_contents(path): #a function to print the directory contents of a give path
    try: #try to run this code without exceptions
        print(f"\n\033[7m{path}:\033[0m") #print the directory path in a very visible way

        for object in os.listdir(path): #iterate through the path given to the function
            fullpath = os.path.join(path,object) #add the current item to the current path to give a testable full path
            if os.path.isdir(fullpath): #check if current item from the listdir is a directory
                list_subdir(fullpath,1) #run the recursive list_subdir() function with a counter of 1
            else: #not a directory
                print(object) #print the name of the file without the rest of the path

    except FileNotFoundError: #a FileNotFoundError occurs
        print("\n\033[7mThat directory does not exist, please try again\033[0m") #print a warning about error
    
    except PermissionError: #PermissionError occurs
        print("\n\033[7mYou do not currently have permission to access this directory\033[0m") #print a warning about error
    
    except IOError: #IOError occurs
        print("\n\033[7mAn unexpected IOError has occurred\033[0m") #print a warning about error
    
    except: #general exception
        print("\n\033[7mAn unexpected error has occurred\033[0m") #print a warning about error

while True: #main loop for menu
    print("\nDirectory Inspector - List all files and subdirectories of a directory") #print statements for program menu
    print("1: Inspect the provided test directory")
    print("2: Provide your own directory to Inspect")
    print("3: Exit")
    choice = input("Which function would you like to execute?: ") #get user's choice

    if choice == '1': #test if user chose 1
        list_directory_contents("Test_Directory") #run list_directory_contents() on the provided test directory
    elif choice == '2': #test if user chose 2 
        user_dir = input("What is the full path to the directory you'd like to Inspect?: ") #get path from the user
        list_directory_contents(user_dir) #run list_directory_contents() with a path from the user
    elif choice == '3': #test if user chose 3
        break #end loop and program
    else: #user made a choice outside of the menu choices
        print("\033[7mThat was not a valid choice, please try again\033[0m")