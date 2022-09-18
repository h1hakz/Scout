import os
import sys
import csv

result = []
allResults = []
inputWord = []
stringFound = []
noOfKeywords = []
keyWordLineNo = []
directoryList = []
lineStringContain = []
stringFoundCount = 0

#Colors and shit like that
white = '\033[97m'
red = '\033[91m'
yellow = '\033[93m'
end = '\033[0m'

# Banner
print('''  %s
   _____                 _   
  /  ___|               | |  
  \ `--.  ___ ___  _   _| |_ 
   `--. \/ __/ _ \| | | | __|
  %s/\__/ / (_| (_) | |_| | |_%s 
  \____/ \___\___/ \__,_|\__|v1%s.%s0%s\n	   powered by h1hakz\n''' % (yellow,red,white,red,white, end))

# Read the keywords from the input file
# Check file size
def readInputFile(file):
	if(os.stat(file).st_size != 0):
		keyfile = open(file)
		nextline = keyfile.readline()

		while nextline != '' and nextline != '\r\n':
			inputWord.append(nextline.strip())
			nextline = keyfile.readline()
		keyfile.close()
		return inputWord
	else:
		return inputWord

# File extention verification
def fileExtentionCheck(blackListFile, fileExt):
	return not(fileExt in blackListFile)

# check argument length
argLength = len(sys.argv)

# check for argument
if argLength != 3:
    print'\n'
    print('Please specify a correct argument: <Project_Directory_Path> <Keyword_File>')
    sys.exit()	
else:
	# Get argument value
	dirPath = sys.argv[1]
	
	# Searched keyword file process
	filename = sys.argv[2]
	
	# list of searched keywords from the input file
	searchedKey = readInputFile(filename)
	if(len(searchedKey) <= 0):
		print 'Searched keyword file is empty!!'
		sys.exit()
	inputWord = []

	# list of blacklist keywords from the input file
	listOfBlackListFile = readInputFile('fileBlackList.txt')

	if(len(listOfBlackListFile) <= 0):
		print 'Black list file is empty!!'
		sys.exit()
	inputWord = []

	print'\nProject Directory Path: ', dirPath
	print'\nSearched Key-Word: ', searchedKey
	
	# Render file name
	for path, subdirs, files in os.walk(dirPath):
		for name in files:
			filepath = os.path.join(path, name)
			extension = os.path.splitext(filepath)[1][1:]
			fileExit = fileExtentionCheck(listOfBlackListFile, extension)

			# Check file size 
			if(os.stat(filepath).st_size != 0 and fileExit):					
				for j in range(0, len(searchedKey)):
					# Number of lines
					numberOfLine = []
					lineString = []
					
					# Read the first line from the file
					f = open(filepath)
					line = f.readline()

					# First line count of the file
					lineNo = 1

					# Loop until EOF
					while line != '' :
						# Search for string in line						
						index = (line.strip().lower()).find(searchedKey[j].lower())
						if ( index != -1) :
							lineString.append(line.strip())
							numberOfLine.append(lineNo)
							stringFoundCount = 1
								
						# Read next line of the file
						line = f.readline()  
						
						# Increment line counter by 1
						lineNo += 1
					if stringFoundCount == 1:
						stringFound.append(searchedKey[j])
						keyWordLineNo.append(numberOfLine)
						lineStringContain.append(lineString)
						stringFoundCount = 0
					
					# Close the file 
					f.close()
					
				# Print file name with line numbers	
				if len(stringFound) > 0:
					directoryList.append(filepath)
					combinedResult = directoryList, stringFound, keyWordLineNo, lineStringContain
					allResults.append(combinedResult)
				
				directoryList = []
				stringFound = []
				keyWordLineNo = []
				lineStringContain = []

if allResults == []:
    print('No result found!')
    sys.exit()	
	
else:
	# Write searched result in CSV file				
	with open('result.csv', 'w') as csvFile:
		fieldName = ['File Path', 'Searched Keyword', 'Line Number', 'Line']
		thewriter = csv.DictWriter(csvFile, fieldnames = fieldName)
		
		# write header in CSV file
		thewriter.writeheader()
		
		for i in range(0, len(allResults)):
			result = allResults[i]
			keyLen = len(result[1])
			
			# Write file path in CSV file
			thewriter.writerow({'File Path' : result[0][0]})
			
			# Write keyword and corresponding searched line numbers
			for j in range(0, keyLen):
				lineLen = len(result[2][j])
				thewriter.writerow({'Searched Keyword' : result[1][j]})
				for k in range(0, lineLen):
					thewriter.writerow({'Line Number' : result[2][j][k], 'Line' : result[3][j][k]})
			result = []
		
		# Close CSV file after processing
		csvFile.close()

	print '\nOpen the result.csv file, to verify the searched results!\n'
