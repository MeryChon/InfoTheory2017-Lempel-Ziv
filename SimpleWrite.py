import sys
import io


def readBitsFromFile(path):
	rFileObject = None
	try:
		rFileObject = io.open(path, "rb")
	except :
		print("Could not open file for reading")
		raise
	rFileContent = rFileObject.read()
	return rFileContent


def bitsToBytes(bits):
	return int(bits, 2).to_bytes((len(bits)+7) // 8, byteorder="big")



def writeToFile(destFilePath, bytes):
	try:
		resFileObject = open(destFilePath, "wb")
	except:
		print("Could not open file for writing")
		raise
	# resFileObject.write(str(bytes)[2:len(str(bytes))-1])
	resFileObject.write(bytes)


def checkAnswers(resFile, checkFile):
	try:
		resFileObject = open(resFile, "rb")
	except:
		print("Could not open file for reading")
		raise
	res = resFileObject.read()
	# print(res)

	try:
		checkFileObject = open(checkFile, "rb")
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
	bits = readBitsFromFile(sys.argv[1])
	bytes = bitsToBytes(bits)
	writeToFile(sys.argv[2], bytes)
	# checkAnswers(sys.argv[2], sys.argv[3])
