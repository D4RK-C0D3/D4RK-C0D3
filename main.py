#!/usr/bin/python

import requests
#import threading

base_url = input('[+]Enter website url: ')

#base_url = 'https://www.w3schools.com/'

dir = ['bootstrap','svg','jquery','sql','html','css','js','javascript','py','python','asp','json','php','c','c++','cpp']

'''class main:
	def find_dir(self):
		f = open('crawl.txt')
		f.readlines()
		for line in f:
			i = line[:-1]
			url = f'{base_url}/{i}'
			r = requests.get(url=url)
			s = int(r.status_code)
			if s == 200:
				print(f'Found: /{i}/')
			else:
				print(f'not Fonud: {i}')

myobj = main()
t1 = threading.Thread(target=myobj.find_dir)
t1.start()
t1.join()
print('the end')
'''

def main():
    for i in dir:
        url = f'{base_url}/{i}'
        r = requests.get(url=url)
        s = int(r.status_code)
            if s == 200:
	        print(f'Found: /{i}/')
	   # else:
	       # print(f'not Fonud: {i}')
main()
