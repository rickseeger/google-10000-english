#!/usr/bin/python 

# generate table of 2^12 simple words

import re

dict_size = 4096
in_file = 'google-10000-english.txt'
out_file = 'dict.txt'
min_len = 4
max_len = 7

vowels = re.compile('[aeiou]')
fin = open(in_file, 'r')
fout = open(out_file, 'w')
count = 0

for line in fin:
    tok = line.strip()
    if (len(tok) >=4 and len(tok) <= 7 and vowels.search(tok) != None):
        count += 1
        fout.write(tok + '\n')
    if (count >= dict_size):
        break

fout.close()
fin.close()

print 'created ' + str(count) + ' words in file \'' + out_file +'\''
