#!/usr/bin/env python
# encoding: utf-8

import sys

def FizzBuzz(number=100):
	for x, x3, x5 in ((i , i%3, i%5) for i in range(1, number)):
		if x3 == 0 and x5 == 0:
			print('FizzBuzz')
		elif x3 == 0:
			print('Fizz')
		elif x5 == 0:
			print('Buzz')
		else:
			print(x)

if __name__ == '__main__':
	number = 100

	if len(sys.argv) >= 2:
		number = int(sys.argv[1])

	FizzBuzz(number)
