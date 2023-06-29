#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def basic():
    print("I am a basic function")

# TODO: function that takes arguments
def argfunction(a, b):
    print(a + b)

argfunction(1,5)
# TODO: function that returns a value
def retfunction(a,b):
    return a+b

print("2 + 3 =", retfunction(2,3))
# TODO: function with default value for an argument
 
def power(num, x=1): #x takes 1 as default when no argument is passed by the user.
        result = 1
        for i in range(x):
            result*=num
        return result
print(power(5))

# TODO: function with variable number of arguments