import CompleteRead
import SimpleWrite
import sys
import time
from math import ceil, log2

class LZDecompressor:
    def __init__(self, in_file, out_file):
        raw = CompleteRead.readBytesFromFile(in_file)
        self.out_f = out_file
        self.bits = str(CompleteRead.removePadding(CompleteRead.bytesToBits(raw)))
        self.file_size, self.compressed = self.get_info()
        self.decompressed = ""
        self.dictionary = {0: "0", 1: "1"}

    def get_info(self):
        n = self.bits.find("1")
        binary_num = self.bits[n:2*n+1]
        file_size = 8*int(binary_num, 2)
        return file_size, self.bits[2*n+1:]

    def decompress(self):
        i = 0
        while i < len(self.compressed):
            size_of_index = ceil(log2(len(self.dictionary)))
            index = int(self.compressed[i:i+size_of_index], 2)
            if index in self.dictionary:
                code = self.dictionary[index]
                self.dictionary.pop(index)
                self.dictionary[index] = code + "0"
                self.dictionary[len(self.dictionary)] = code + "1"
                self.decompressed += code
            i += size_of_index
        self.decompressed = self.decompressed[:self.file_size]

    def write_to_file(self):
        bytes_to_write = SimpleWrite.bitsToBytes(self.decompressed)# CompleteWrite.addPadding(self.decompressed)
        SimpleWrite.writeToFile(self.out_f, bytes_to_write)


if __name__ == '__main__':
    decompressor = LZDecompressor(sys.argv[1], sys.argv[2])
    decompressor.decompress()
    decompressor.write_to_file()
