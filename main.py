#!/usr/bin/env python3

############*****Importing Modules*****############

import random as _random # for making random passwords.
import sys as _sys # for taking command line arguments.
import getopt as _getopt # for making command line flags.
import json as _json


############*****String Decleration*****############

_sm_Letter = ['abcdefghijklmnopqrstuvwxyz'] # small letters to use as a string on the user's password.
_cap_Letter = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'] # capital letters to use as a string on the user's password.
_sp_char = ['!?,:;()-/@_`~#$%=^+&{*}[]|<>\.'] # special charecters to use as a string on the user's password.
_Numbers = ['0','1','2','3','4','5','6','7','8','9'] # numbers to use as a string on the user's password.
_str = _sm_Letter + _cap_Letter + _Numbers + _sp_char # concatinating those lists
_str = ''.join(_str)
_str = _str*100


############*****Defining Command line Options*****############

_args = _sys.argv[1:] # Remove 1st argument (file name) from the list of command line arguments. 
_s_opt = "ahvl:um:" # short options
_l_opt = ["accounts","help","masterkey=","lenght=","version","update"] # long options


############*****Defining Some Imyportant stuffs*****############

def _usage(): #defining usage
	print ("Usage: "+ _sys.argv[0] + " -m [MASTERKEY]\n")
	print ("Example: "+ _sys.argv[0] + " -m your_master_key\n")
def _help(): #defining help section
	_usage()
	print ("A tool for generate random and strong encrypted password and to keep that password also.\n\nMandatory arguments to long options are mandatory for short options too.")
	print ("-a, --accounts			to know how many accounts are exists.")
	print ("-h, --help			you are now seeing this.")
	print ("-l, --lenght			to pass the lenght of your password.")
	print ("-v, --version			to see the version of this tool.")


############*****Creating Masterkey Genaration Algorithum*****############

def _create_Master_Key():
	_masterKey = _random.sample(_str, 1000)
	_masterKey = ''.join(_masterKey)
	print('\nYour password is : '+_masterKey)



############*****Trying To Get Info From The User From The Command Line Arguments*****############

try:
	# Parsing argument
	arguments, values = _getopt.getopt(_args, _s_opt, _l_opt)
	# checking each argument
	for currentArgument, currentValue in arguments:
		if  currentArgument in ("-a", "--accounts"):
			pass
			exit()
		elif currentArgument in ("-h", "--help"):
			_help()
			exit()
		elif currentArgument in ("-v", "--version"):
			print('Version: V1.0.0')
			exit()
		elif currentArgument in ("-l", "--lenght"):
			_pass = _random.sample(_str, int(currentValue))
			_pass = ''.join(_pass)
			print('\nYour password is : '+_pass)
			exit()
		elif currentArgument in ("-m", "--masterkey"):
			print ("Displaying file_name:", _sys.argv[0])
		#elif currentArgument in ("-v", "--version"):
		#	print (("Enabling special output mode (% s)") % (currentValue))
except _getopt.error as err: 		
	# output error, and return with an error code		
	print (str(err))
	print ("Enter -h, --help for help.")
	exit()
	



############*****Taking Info From The User Manually and generating random password*****############

_info = {}
try:
	_len_string = int(input('Enter the lenght of your password :> ')) # for getting the lenght of the user's password.
except:
	print('Please enter valid info')
	exit()
	
def _main():
	_pass = _random.sample(_str,_len_string)
	_pass = ''.join(_pass)
	print('\nYour password is : '+_pass)
	_ans = input('\nDo you want to keep this password[Y/N] :> ')
	if  _ans == 'Y' or _ans == 'y' :
		_user = input('\nEnter User Name :> ')
		_acc_Name = input('\nEnter Account Name :> ')
		_email = input('\nEnter Email :> ')
		_info[_acc_Name] = {
			'name': _user,
			'email': _email,
		 	'pass': _pass
		}
		s = _json.dumps(_info, indent=2)
		with open('output.json', 'a') as f:
			f.write(s)		
			exit()
	elif _ans == 'N' or _ans == 'n' :
		_main()
		exit()
	else:
		print('Please enter valid info')
		exit()
		
if __name__ == '__main__':
	_main()
	_create_Master_Key()