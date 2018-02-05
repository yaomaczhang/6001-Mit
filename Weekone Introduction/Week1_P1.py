"""Assume s is a string of lower case characters.

 Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

 Number of vowels: 5 """
 
s='azcbobobegghakl'
mynum=0
for c in s.lower():  # s.lower() turn all letter into lower cases, don't forget the ()
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
        mynum+=1
print("Number of vowels:",mynum)
