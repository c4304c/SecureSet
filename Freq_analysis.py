#!/usr/bin/python3

#import Coounter
from collections import #Counter

#Use file in Script
file = open("/home/chris/Desktop/CRY100_01_Lab_Substitution.txt", "r").read()

#remove spaces
file2 = file.replace(' ','')#remove whitespace
#view Text
print(file2)

#Get Frequency Analysis Results
count = list(file) 
c = Counter(count)
print (c)










