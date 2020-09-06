#!/usr/bin/python3
#Verify HMAC, output matching HMAC entries to one file and non-matching HMAC entries to another file

import hmac
import sys

#create Hash of Message with key in hex:
def gen_tag(msg, key):
    hm = hmac.new(key.encode())
    hm.update(msg.encode())
    return hm.hexdigest()

#Open messages and key to use
with open('CRY100_05_Lab_tags.txt') as x:
    line = x.read().splitlines()
with open("CRY100_05_Lab_master.key") as x:
    key = x.read()

strNtag = []

#split strings and tags into pairs
for x in line:
    pairs = x.split(":")
    strNtag.append((pairs[0], pairs[1]))

# open files for results
wrong = open('wrong.txt', 'w')
wrong.write("DOES NOT MATCH"'\n')
right = open('correct.txt', 'w')
right.write("MATCHES"'\n')

# Compare Hashes and add results to files
for line in strNtag:
    RIGHThash = gen_tag(line[0], key)
    if RIGHThash != line[1]:
        wrong.write("Message: ""{}\n".format(line[0]))
        wrong.write("Wrong Hash: ""{}\n".format(line[1]))
        wrong.write("Correct Hash: ""{}\n".format(RIGHThash)) 
    else:
        right.write("Message: ""{}\n".format(line[0]))
        right.write("Correct Hash: ""{}\n".format(RIGHThash))
wrong.close()
right.close()

