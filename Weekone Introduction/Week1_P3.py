"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

s='azcbobobegghakl'
c='' 
for n in range(len(s)-1):
    if s[n]<=s[n+1]:
        c+='1'
    else:
        c+='0' # made a string, 10010101111011, the goal becomes how to find the longest 1111
for i in range(1,len(c)+1): # assume i is the length of the string
    for j in range(len(c)+1-i): #assume j is the start position of the string
        if c[j:j+i]=='1'*i:
            start=j
            length=i
            break
print("Longest substring in alphabetical order is:",s[start:start+length+1])