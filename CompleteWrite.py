import sys
import io


def readBits(sourceFilePath):
	rFileObject = None
	try:
		rFileObject = io.open(sourceFilePath, "r")
	except :
		print("Could not open file for reading")
		raise
	rFileContent = rFileObject.read()
	return rFileContent




def addPadding(bits):
	bits += "1"
	while not (len(bits)%8 == 0):
		bits += "0"

	resInBytes = int(bits, 2).to_bytes((len(bits)+7) // 8, byteorder="big")
	return resInBytes


def writeToFile(destFilePath, bytes):
	try:
		resFileObject = open(destFilePath, "wb")
	except:
		print("Could not open file for writing")
		raise
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
	bits = readBits(sys.argv[1])
	bytes = addPadding(bits)
	writeToFile(sys.argv[2], bytes)
	# checkAnswers(sys.argv[2], sys.argv[3])
