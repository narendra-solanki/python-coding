#!/usr/bin/env python3

# A program to print list of prime numbers
def is_prime_number(number):
	#any number less than 2 is not prime number
	if number < 2:
		return False
	#check if number is divisible by any of the number less than itself
	for x in range(2,number):
		#if number is divisible than its not prime
		if(number%x == 0):
			return False	
	return True

def list_primes(count):
	#run a for loop from 1 to 'count'-1
	for x in range(count):
		if is_prime_number(x) is True:
			print(x, end = ' ', flush=True) #end each print statement in whitespace instead of new line	
	print()	#print newline after printing whole list


if __name__ == '__main__': list_primes(101)
	

