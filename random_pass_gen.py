#!/bin/python
import string
import random


def err():
	print('Error! Please enter some valid info.')
	exit()

def userInput(val, asciiStr):
	
	if val == 'Y' or val == 'y':
		s.extend(asciiStr)
	elif val == 'N' or val == 'n':
		pass
	else:
		err()

def passGen(string):
	string = "".join(string)
	try:
		retPass = random.sample(string, int(len))
		retPass = "".join(retPass)
		print(retPass)
	except:
		err()


if __name__=='__main__':
	s1 = list(string.ascii_lowercase)
	s2 = list(string.ascii_uppercase)
	s3 = list(string.digits)
	s4 = list(string.punctuation)

	len = input('Enter Password Lenght:')
	s = []
	if len.isdigit() :
		ans0 = input('Do You want to use all printable characters:[Y/N] ')
		if ans0 == 'Y' or ans0 == 'y':
			s.extend(list(s1))
			s.extend(list(s3))
			s.extend(list(s3))
			s.extend(list(s4))
		elif ans0 == 'N' or ans0 == 'n':
			ans1 =	input('Do You want to use small letters:[Y/N] ')
			userInput(ans1, s1)
			ans2 =	input('Do You want to use capital letters:[Y/N] ')
			userInput(ans2, s2)
			ans3 =	input('Do You want to use numbers:[Y/N] ')
			userInput(ans3, s3)
			ans4 =	input('Do You want to use special characters:[Y/N] ')
			userInput(ans4, s4)
		else:
			err()
		passGen(s)
	else:
		err()