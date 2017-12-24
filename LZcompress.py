import sys
import SimpleRead
from math import ceil, log2
import time

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
        # print(bits)
        return bits

    def get_gamma(self, num):
        binary_num = '{0:b}'.format(num)
        gamma = '0' * (len(binary_num) - 1) + binary_num
        print("gamma code is ", gamma)
        return gamma

    def compress(self):
        i = 0
        while True:
            if i > len(self.bits_array):
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
        to_write += "0"
        while not (len(to_write) % 8 == 0):
            to_write += "0"
        # print(to_write)
        res = int(to_write, 2).to_bytes((len(to_write) + 7) // 8, byteorder="big")
        out_f_obj = open(self.out_f, 'wb')
        out_f_obj.write(res)
        out_f_obj.close()
        # SimpleRead.writeToFile(self.out_f, res)

    def get_longest_prefix(self, i):
        max_key = ""
        bit_substr = self.bits_array[i:]
        for d in self.dictionary:
            if bit_substr.startswith(d):
                return d
        while max_key == "":
            bit_substr += "0"
            for d in self.dictionary:
                if bit_substr.startswith(d):
                    return d


if __name__ == '__main__':
    s = time.time()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    compr = LZCompressor(input_file, output_file)
    compr.write_to_file()
    print(time.time()-s, " seconds elapsed ")
