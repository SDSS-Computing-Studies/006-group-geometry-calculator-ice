#!python3
# Volume Calculator
# Feel free to rename your variables

import math
from typing import List

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
    return None


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
    
def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    
    #r=input("enter the radius: ") # sphere, cylinder, cone
    #s=input("enter the slant height: ")
    #h=input("enter the height: ") # cube, retangle, pyramid
    #w=input("enter the width")
    #l=input("enter the langth")
    # triangle
    #baselength=input("enter the height of the base of a surface of a triangle (calulate the area of the): ")
    #baselength=input("enter the length of one side of a surface of a triangle: ")

     prompts=["enter the radius: ","enter the height:","enter the width: ","enter the length: ","enter the height of the base of the surface of the triangle: ","enter the length of one side of the surcace of the triangle: "]
    
    r,h,w,l,baseheight,baselength,=prompts
    if shape=="sphere":
        question=[r]
        return question
    elif shape=="cylinder":
        question=[r,h]
        return question
    elif shape=="cone":
        question=[r,h]
        return question
    elif shape=="cube":
        question=[w]
        return question
    elif shape=="cuboid":
        question=[h,w,l]
        return question
    elif shape=="pyramid":
        question=[h,w,l]
        return question
    elif shape=="triangular prism":
        question=[baseheight,baselength,h]
        return question
    else:
        question=[0]
        return question


def getInputs(question):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape

    a=0
    List=[]
    for i in question:
        if question[a]==0:
            break
        else:
            c=input(question[a])
            c=float(c)
            List.append(c)
            a+=1
        return List

        def Calculate(measuremnets,shhere):

            if shape=="sphere":
                v=(4*math.pi*(measuremnets[0]**3))/3
                return vars
            elif shape=="cylinder":
                v=math.pi*(measurements[0]**2)*measurements[1]
                return vars
            elif shape=="cube":
                v=

 

    
    
 
   
def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    
    triangle=getShape()
    # get list of questions
    questions=getparams(shape)
    # get list of measurements 
    measuremnets=getInputs(questions)
    print("value is "+str(calculate(measuremnets,shape))) # calculate the volume 



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