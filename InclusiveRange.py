#!/usr/bin/env python3

# An implementation of range() method which will include the last number
def main():
	#generate from 0 to 5
	for num in inclusive_range(5):
		print(num, end=' ', flush=True)
	else: #print new line at the end of for loop
		print()

	#generate from 5 to 10
	for num in inclusive_range(5, 10):
		print(num, end=' ', flush=True)
	else: #print new line at the end of for loop
		print()

	#generate number in step of 5
	for num in inclusive_range(5, 25, 5):
		print(num, end=' ', flush=True)
	else: #print new line at the end of for loop
		print()

	

# function to generate numbers inclusive of given number
def inclusive_range(*args):
	numargs = len(args)
	start = 0
	step = 1

	if numargs < 1:
		raise TypeError(f'Need atleast one argument to generate numbers, got {numargs}')
	elif numargs == 1:
		stop = args[0]
	elif numargs == 2:
		(start, stop) = args		
	elif numargs == 3:
		(start, stop, step) = args
	else:
		raise TypeError(f'Max 3 arguments are allowed, got {numargs}')

	#generator logic
	i = start
	while i <= stop: #generate numbers till we hit stop
		yield i
		i = i + step




if __name__ == '__main__': main()