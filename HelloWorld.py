#!/usr/bin/env python3

import platform;

#This is my very first program in Python language


# main() function for this program
def main():
	#message()
	useOfVariable(); print()
	conditionalStatement(); print()
	useOfPrint(); print()
	blockAndScope(); print()
	useOfLoops(); print()
	defaultParameter(); print()
	defaultParameter("Parameter passed"); print()

	print('Demo of a class')
	#donald = Duck(sound = "quack", swag = "Walk")
	donald = Duck()
	print(donald.sound())
	print(donald.swag())
	#toString() method demo
	print(donald)
	print()

	print('Demo of variable types')
	demoTypes(); print()

	
	print('Demo of str class methods')
	demoStringClass(); print()

	print('Demo of sequence types')
	demoSequenceTypes(); print()

	print('Demo of ternary operator')
	demoTernary(); print()

	print('Demo of variable arguments in function')
	args = ('one','two')
	variableArgs(*args); print()

	print('Demo of keyword arguments in function')
	dictObject = dict(One = '1', Two = '2')
	keywordArgs(**dictObject); print()

	print('Demo of file operations')
	obj = FileOps()
	obj.readFile('InclusiveRange.py')
	print()

	


#Print version of this python interpreter
def message():
	print('Hello World')
	print('This is my first Python program')
	print('Version of python is {}'.format(platform.python_version()))

#function demonstrating use of a variable
def useOfVariable():
	version = platform.python_version()
	print('Version of Python is {}'.format(version))

#function demonstrating use of a conditional statement
def conditionalStatement():
	condition = False
	if condition:
		print('Condition is true')
	elif condition == False:
		print('Condition is false')
	else:
		print('Condition is false')

#different uses of print function
def useOfPrint():
	number = 14
	string = 'The number is {}'.format(number)
	print(string)
	#use of f string
	print(f'Printing number using "f" string : {number}')

def blockAndScope():
	x=42
	y=73

	if(x < y):
		print(f'x < y: x is {x} and y is {y}')
		z = 112
	print('Variable scope is not confined to a block')
	print(f'Value of z outside block is {z}')

#function demonstrating use of while and for loop
def useOfLoops():
	words = ['one','two','three','four','five']
	n=0
	#use of while loop
	print('Printing list using while loop')
	while(n < 5):
		print(words[n])
		n+=1
	#use of for loop
	print('\nPrinting list using for loop')
	for word in words:
		print(word)

#function to use default value of parameter
def defaultParameter(param = "Default Parameter"):
	print(param)

#demo of variable types
def demoTypes():
	x = 7
	print(f'Type of {x} is: {type(x)}')
	x = 7.0
	print(f'Type of {x} is: {type(x)}')
	x = '7'
	print(f'Type of "{x}" is: {type(x)}')
	x = True
	print(f'Type of {x} is: {type(x)}')
	x = None
	print(f'Type of {x} is: {type(x)}')

#demonstration of class in Python
class Duck:	

	def __init__(self, **kwargs):
		self._sound = kwargs['sound'] if 'sound' in kwargs else 'Quaaack'
		self._swag = kwargs['swag'] if 'swag' in kwargs else 'Walking like a duck'

	#getter/setter method for sound
	def sound(self, sound = None):
		if sound: self._sound = sound
		return self._sound

	#getter/setter method for swag
	def swag(self, swag=None):
		if swag : self._swag = swag
		return self._swag
	#create a toString() method
	def __str__(self):
		return f'sound is {self.sound()} and swag is {self.swag()}'

def demoStringClass():
	string = 'seveN'
	print(f'Capitalize {string} : {string.capitalize()}') #capitalize first letter
	print(f'Uppercase {string} : {string.upper()}') #uppercase string
	print(f'Lowercase {string} : {string.lower()}') #lowercase string

def demoSequenceTypes():
	#demo of a list
	x = [1,2,3,4,5] #this is a list
	print('print a list {}'.format(x))
	for i in x:
		print(i, end = ' ', flush=True)
	print('\nList is mutable type')
	x[2] = x[2]*10
	for i in x:
		print(i, end = ' ', flush=True)
	print()
	
	#demo of Tuple type
	y = (1,2,3,4,5)
	print('print a tuple {}'.format(y))
	for i in y:
		print(i, end = ' ', flush=True)
	print('\nTuple is immutable type')
	print()

	#demo of range
	z = range(5)
	print('print a range range(5)')
	for i in z:
		print(i, end = ' ', flush=True)
	print()

	z = range(2,7)
	print('print a range {}'.format(z))
	for i in z:
		print(i, end = ' ', flush=True)
	print()

	a = range(2, 50, 5) #increase number by step 5
	print('print a range with step {}'.format(a))
	for i in a:
		print(i, end = ' ', flush=True)

	print('\nDemo of dictionary')
	dict = {'one':1,'two':2,'three':3,'four':4,'five':5}
	for key, value in dict.items():
		print(f'key: {key}, value: {value}')

def demoTernary():
	hungry = False
	x = 'Feed the baby' if hungry else 'Let him play'
	print(x)

def variableArgs(*args):
	if len(args):
		for arg in args:
			print(f"arg is {arg}")

def keywordArgs(**kwargs):
	if len(kwargs):
		for k in kwargs:
			print(f"{k} is {kwargs[k]}")

class FileOps:
	def readFile(self, file = 'Fibonacci.py' ):
		#open the file
		f = open(file)
		#read the file
		for line in f:
			print(line.rstrip())




	

#execute program from main() function
if __name__ == '__main__': main()


