#!python3
# Volume Calculator
# Feel free to rename your variables

import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: sepehr
    # Modified: Sepehr Zolfaghari
    print("Volume Calculator")
    print("author: Sepehr Zolfaghari")
    print("modified by Sepehr Zolfaghari")
    print("/n")
    return none

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Sepehr 
    # Modified: Sepehr Zolfghari
    print("start")

    print("instructions: ")
    print("This program will be asking you to enter a shape that you would want to calculate its volume")
    print("Then you need to enter that right measuremnets that you will use")
    print("The volume would be the answer")
    print("/n")
    print("Enter yes to remake the program")
    print("Enter no to close the program")
    print("/n")
    print("Shapes accessible: ")
    print("/n")
    print("sphere, cylinder, cone, cube, cuboid, pyramid, triangular prism")
    print("/n")
    return None

def getShape():
    # input: none needed
    # output: string shape
    # author
    shape=input("enter a shape: ")
    return shape


 

    
    
 
   
def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    
    shape=getShape()
    # get list of questions
    questions=getParams(shape)
    
    

main()
while True:
    print("\n")
    a=input("continue? yes or no: ")
    print("\n")
    if a == "yes":
        main()
    else:
        print("end")
        break