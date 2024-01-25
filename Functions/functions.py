#Programmer: Hayden Coates
#Program: Functions
#Date: 1.19.2024s

def nl(): #New Line Function
		print('\n')


def  who_am_i():  #this a function w/out parameters
		name = 'Hayden C' #local Variable
		age = 16 #local variable
		print('My name is',name,'and im',age,'years old.')

who_am_i()

nl()

def add_one_hundred(num): # num is a parameter
		print(num + 136)
		
add_one_hundred(47864) #47864 is the argument which inserts itself into the Parameter.

nl()

add_one_hundred(0)

nl()

def divide(x,y):
		print(x // y)
		
divide(100000000000,99999999999)

nl()
