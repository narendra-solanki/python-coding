#!/usr/bin/env python3

#program to print fibonacci numbers till nth position

def fibonacci(position = 10):
	counter = 1
	a,b = 0,1 #initialize initial numbers
	while counter <= position:
		print(b, end = ' ', flush=True) #print list of numbers separated by whitespace
		a, b = b, a+b #this statement assigns values to a and b simultaneously
		counter+=1
	print()

if __name__ == '__main__': fibonacci()