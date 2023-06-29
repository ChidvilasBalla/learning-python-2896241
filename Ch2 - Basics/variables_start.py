# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a global string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}
myset = {"a", 1, 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)
# print(myset)

print(mylist[0:5:2]) #prints every 2nd element from 0 to 5
print(mylist[::-1]) #prints the list in reverse order
print(mydict["one"]) #prints the value of the key "one" in the dictionary

print("string type" + str(123)) #string can concatenate with string only

# re-declaring a variable works

# to access a member of a sequence type, use []

# use slices to get parts of a sequence

# you can use slices to reverse a sequence

# dictionaries are accessed via keys

# ERROR: variables of different types cannot be combined

# Global vs. local variables in functions

def someFunction():
    mystr = "This is a local string"
    print(mystr)

someFunction() #prints the local variable mystr
print(mystr) #prints the global variable mystr    