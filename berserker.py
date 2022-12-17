import binascii
import argparse
import subprocess
import os
import sys
import re
import time
import re
try:
    subprocess.Popen(['figlet', 'Berserker ! '])
except(FileNotFoundError):
    print ("You need to install Figlet ma boii !")

try:
    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED + "Created by : salmane zwin" + CEND)
    print(CRED + "Github : https://github.com/dreccanus \nTwitter : https://twitter.com/dreccnus" + CEND)
except():
    print ("error")
parser = argparse.ArgumentParser(description ='Berserker Encoder/Decoder !!\n python3 --encrypt [String]\n --decrypt [string]')

parser.add_argument('--encrypt', '-e', type = str, help ='Encrypt the text')
parser.add_argument('--decrypt', '-d', type = str, help ='Decrypt the text')


if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)
else:
    args = parser.parse_args()


def encrypt():
    value = (args.encrypt)
    jj = (binascii.hexlify(value.encode("utf-8")))
    jj2 = jj.decode()
    jj3 = (jj2[::-1])
    output = ''
    for c in jj3:
        h = ("{:08b}".format(ord(c)))

        output += h

    lmqawed = (output[::-1])
    modified_string1 = re.sub(r'[1]', 'x', lmqawed)
    modified_string1 = re.sub(r'[0]', ':', modified_string1)
    finiiisyo = (modified_string1)
    def run_length_encode(string):
        encoded_string = ""
        current_char = string[0]
        char_count = 1
        for i in range(1, len(string)):
            if string[i] == current_char:
                char_count += 1
            else:
                encoded_string += current_char + str(char_count)
                current_char = string[i]
                char_count = 1
        encoded_string += current_char + str(char_count)
        return encoded_string

    string = (finiiisyo)
    print ("==> "+string)


def decrypt():
    try:
        string = args.decrypt
        modified_string1 = re.sub(r'[x]', '1', string)
        modified_string1 = re.sub(r'[:]', '0', modified_string1)
        sting_rv = modified_string1[::-1]
        steee2nin = (sting_rv)
        hex_string = ''.join(hex(int(x, 2))[2:] for x in steee2nin.split())
        decoded_string = binascii.unhexlify(hex_string).decode()
        wwe = (decoded_string[::-1])
        decoded_string = bytes.fromhex(wwe).decode()
        print ("==> "+decoded_string)
    except(ValueError):
        print ("Syntax error")

if args.encrypt:
    encrypt()

elif args.decrypt:
    decrypt()
