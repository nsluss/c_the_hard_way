import sys
import os

def main(argv):
	if argv[0] == "help":
		print("1) Move to directory where your projects are.")
		print("2) type: python exwork.py [name of new directory]")
		print("3) cd to the new  directory. Begin the next lesson of C The Hard Way, Makefile  ready to go!")
	else:
		os.mkdir(os.getcwd()+"/"+argv[0])
		print("Created a new directory at: "+os.getcwd()+"/"+argv[0])
		
		f = open(argv[0]+'/Makefile','w')
		for l in makefile():
			f.write(l)
		f.close()
		print("Created a new default Makefile in that directory")
			
def makefile():
	mk =[
	"CFLAGS=-Wall -g",
	"clean:",
	"     rm -f ex1",
	]
	return mk

if __name__ == "__main__":
	main(sys.argv[1:])
