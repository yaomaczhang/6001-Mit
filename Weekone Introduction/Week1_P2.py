"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
s = 'azcbobobegghakl'
count=0
for n in range(len(s)-2): # the last section is s[len(s)-3:len(s)]
    if s[n:n+3]=="bob":
        count+=1
print("Number of times bob occurs is:",count)