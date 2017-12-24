import sys
import io
import bitarray



def readBytesFromFile(path):
	try:
		fileObject = io.open(path, "rb")
	except:
		print("Could not open file for reading")
		raise
	fileContent = fileObject.read()
	return fileContent


def bytesToBits(bytes):
	ba = bitarray.bitarray()
	ba.frombytes(bytes)
	return ba
	


def removePadding(bits):
	strbits = str(bits)
	strbits = strbits[10:len(strbits)-2]
	i = len(strbits)-1
	for i in range(len(strbits)-1, 0, -1):
		if(strbits[i] == "1"):
			break
	res = strbits[0:i]
	return res



def writeToFile(destFilePath, result):
	resFileObject = None
	try:
		resFileObject = open(destFilePath, "w")
	except:
		print("Could not open file for writing")
		raise	
	resFileObject.write(result)





def checkAnswer(resFile, answerFile):
	try:
		resFileObject = open(resFile, "r")
	except:
		print("Could not open file for reading")
		raise
	res = resFileObject.read()
	# print(res)

	try:
		checkFileObject = open(answerFile, "r")
	except:
		print("Could not open file for reading")
		raise
	check = checkFileObject.read()
	# print(check)

	if check == res:
		print("YAAAY")
	else:
		print("NOOO")





if __name__ == "__main__":
	bytes = readBytesFromFile(sys.argv[1])
	bits = bytesToBits(bytes)
	res = removePadding(bits)
	writeToFile(sys.argv[2], res)
	# checkAnswer(sys.argv[2], sys.argv[3])