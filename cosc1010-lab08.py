# Peyton Roswadovski
# UWYO COSC 1010
# Submission Date: 11/10/24
# Lab Section:14
# Sources, people worked with, help given to: Lab TAs
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def check_int_or_float(string):
    returnValue = False
    try:
        returnValue = float(string)
        returnValue = int(string)
    except:
        pass
    return returnValue


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, lx, ux):
    m_number = check_int_or_float(m)
    b_number = check_int_or_float(b)
    lx_number = check_int_or_float(lx)
    ux_number = check_int_or_float(ux)

    print(m_number, b_number,lx_number, ux_number)
    if ((m_number or m_number == 0) and (b_number or b_number == 0) and (lx_number or lx_number == 0) and (ux_number or ux_number == 0)):
        y_arr = []
        for x in range(lx_number,ux_number):
            y = m_number * x + b_number
            y_arr.append(y)
        return y_arr
    else:
        print("one or more of your values are invalid")


while True: 
     m = input("give me an m")
     if (m == "exit"):
        break
     b = input("give me a b")
     if (b == "exit"):
        break
     lx = input("give me a lower x bound")
     if (lx == "exit"):
        break
     ux = input("give me an upper x bound")
     if (ux == "exit"):
        break
     print(slope_intercept(m,b,lx,ux))
   

print("*" * 75)
#     
# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quadratic_formula(a,b,c):
    a_number = check_int_or_float(a)
    b_number = check_int_or_float(b)
    c_number = check_int_or_float(c)

    answers = []

 answer1 = -b_number + **4*a_number*c_number/2*a_number
 answer2 = -b_number - **4*a_number*c_number/2*a_number