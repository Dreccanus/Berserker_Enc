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
parser = argparse.ArgumentParser(description ='Berserker Encoder !!\n python3 --encrypt [String]')

parser.add_argument('--encode', '-e', type = str, help ='Encode the text')



if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)
else:
    args = parser.parse_args()



value = (args.encode)
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
print (string)
