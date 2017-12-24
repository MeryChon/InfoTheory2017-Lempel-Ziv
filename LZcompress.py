import sys
import SimpleRead
from math import ceil, log2
import time
import CompleteWrite

class LZCompressor:
    def __init__(self, in_file, out_file):
        self.in_f = in_file
        self.out_f = out_file
        self.in_bits = self.get_input_bits()
        self.bits_array = str(self.in_bits)[10:-2]
        self.gamma_length = self.get_gamma(int(len(self.in_bits)/8))
        self.compressed = ""
        self.dictionary = {"0": 0, "1": 1}
        self.compress()

    def get_input_bits(self):
        initial_bytes = SimpleRead.readBytesFromFile(self.in_f)
        bits = SimpleRead.bytesToBits(initial_bytes)
        return bits

    def get_gamma(self, num):
        binary_num = '{0:b}'.format(num)
        gamma = '0' * (len(binary_num) - 1) + binary_num
        return gamma

    def compress(self):
        i = 0
        while True:
            if i >= len(self.bits_array):
                break
            key = self.get_longest_prefix(i)
            b_index = '{0:b}'.format(self.dictionary[key])
            size_of_index = int(ceil(log2(len(self.dictionary))))
            self.compressed += "0" * (size_of_index - len(b_index)) + str(b_index)
            self.dictionary[key + "0"] = self.dictionary[key]
            self.dictionary.pop(key)
            self.dictionary[key + "1"] = len(self.dictionary)
            i += len(key)

    def write_to_file(self):
        to_write = self.gamma_length + self.compressed
        bytes_to_write = CompleteWrite.addPadding(to_write)
        CompleteWrite.writeToFile(self.out_f, bytes_to_write)

    def get_longest_prefix(self, i):
        prefix = ""
        length_of_substr = len(self.bits_array[i:])
        for j in range(0, length_of_substr):
            prefix += self.bits_array[i+j]
            if prefix in self.dictionary:
                return prefix
        # prefix was not in the dictionary, need to append 0-s
        while not (prefix in self.dictionary):
            prefix += "0"
        return prefix


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    compr = LZCompressor(input_file, output_file)
    compr.write_to_file()
