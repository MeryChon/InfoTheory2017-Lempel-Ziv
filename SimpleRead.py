import sys
import io
import bitarray


def readBytesFromFile(path):
	try:
		fileObject = io.open(path, "rb")
	except :
		print("Could not open file for reading")
		raise
	fileContent = fileObject.read()
	return fileContent


def bytesToBits(bytes):
	ba = bitarray.bitarray()
	ba.frombytes(bytes)

	return ba

def writeToFile(resFile, bitarr):
	try:
		resFileObject = open(resFile, "w")
	except:
		print("Could not open file for writing")
		raise
	res = str(bitarr)
	res = res[10:len(res)-2]
	resFileObject.write(res)


def checkAnswer(resFile, answerFile):
	try:
		resFileObject = open(resFile, "r")
	except:
		print("Could not open file for reading")
		raise
	res = resFileObject.read()

	try:
		checkFileObject = open(answerFile, "r")
	except:
		print("Could not open file for reading")
		raise
	check = checkFileObject.read()

	if check == res:
		print("YAAAY")
	else:
		print("NOOO")


if __name__ == "__main__":
	bytes = readBytesFromFile(sys.argv[1])
	bits = bytesToBits(bytes)
	writeToFile(sys.argv[2], bits)
	# checkAnswer(sys.argv[2], sys.argv[3])
