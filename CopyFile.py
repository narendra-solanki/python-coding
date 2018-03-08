#!/usr/bin/env python3

# a function to make a copy of file
def copyTextFile(inFile, outFile):
	infile = open(inFile, "rt") #open input file in read only and text mode
	outfile = open(outFile, 'wt') #open output file in write only and text mode

	#read ech line from input file and copy it to outfile
	for line in infile:
		print(line.rstrip(), file=outfile)
		print('.', end='',flush=True) #show progress bar on console
	#close both input and output files
	outfile.close()
	infile.close()
	print(f'\nfile "{inFile}" copied to "{outFile}"')

def copyBinFile(inFile, outFile):
	infile = open(inFile, "rb") #open input file in binary mode
	outfile = open(outFile, "wb") #create a new file in binary mode

	while True:
		buf = infile.read(8192) #read 8KB of file at a time
		if buf:
			outfile.write(buf)
		else:
			break
	outfile.close()
	infile.close()
	print(f'\nFile "{inFile}" copied to "{outFile}"')



if __name__ == '__main__': 
	copyTextFile('HelloWorld.py', 'copiedFile.py') #copy text file
	copyBinFile('video.mp4','copy of video.mp4') #copy binary file