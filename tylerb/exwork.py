import sys
import os

def main(argv):
	if argv[0] == "help":
		print("1) Move to directory where your projects are.")
		print("2) type: python exwork.py [name of new directory]")
		print("3) cd to the new  directory. Begin the next lesson of C The Hard Way, Makefile  ready to go!")
	else:
		newdir = makeDir(os.getcwd(), argv[0])
		print("Created a new directory at: "+newdir)
		
		createMakeFile(newdir)
		print("Created a new default Makefile in that directory")
		
		#createMakeFile(os.getcwd())

def getFileContents():
	mk =[
	"CFLAGS=-Wall -g\n",
	"clean:\n",
	"\trm -f ex1",
	]
	return mk

def makeDir(cwd,fname):
	directory = cwd+"/"+fname
	os.mkdir(directory)
	return directory

def createMakeFile(dirname):
	f = open(dirname+'/Makefile','w')
	for l in getFileContents():
		f.write(l)
	f.close()

if __name__ == "__main__":
	main(sys.argv[1:])
