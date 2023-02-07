#logic libraries
import itertools, sys

#visual libraries
import pyfiglet
from termcolor import colored


def header():
	t = pyfiglet.figlet_format("Username Generator", font = "digital", justify = "center" )
	print()
	print(colored(t, attrs = ['bold']))
	print("""
		Given a first and last name, and date of birth, outputs a long list of possible usernames.
		For security purposes, consider using a fake name and date of birth.
		v 1.0.
		written by Substing as a project for the OSSSSC.
		""")
	print()

def main():

	header()
	#name variables
	fname = str(input("Enter first name > "))
	lname = str(input("Enter last name > "))
	dob = str(input("Enter date of birth > "))



	#lowercase the data
	fname = fname.lower()
	lname = lname.lower()
	dob = dob.lower()

	#all substrings of name and dob
	f_list = [fname[:i+1] for i in range(len(fname))]
	l_list = [lname[:i+1] for i in range(len(lname))]
	dob_list = [dob[i::] for i in range(len(dob))]

	dividers = ['', '.', '_']


	#start by ignoring order: connect them in order first, last, dob
	#also ignore trivial cases for characters... basically there must be a value for each.

	tupnames = list(itertools.product(f_list, l_list, dob_list))

	unames = []

	#need top join all the tuples into strings along the dividers
	print(colored("\t[+] Generating now...\n", 'green'))
	for d in dividers:
		for t in tupnames:
			unames.append((d.join(t)))


	[print(n) for n in unames]
	print(colored("\n\t[+] Process finished.", 'green'))

try: main()
except KeyboardInterrupt:
	print(colored("\n\t[-] Quitting...", 'red'))