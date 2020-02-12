# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:32:01 2020

@author: kisho
"""

# 1 REVERSE THE STRING 
word = "Kishore" 
print(word[::-1])
word = "kishore"[::-1]
print(word)
 
# 2 SWAP THE CASES 
word = "KiSHorE"
print(word.swapcase())

word = "KiSHorE"
name = []
for i in word: 
    if i.isupper():
        name.append(i.lower())
    elif i.islower():
        name.append(i.upper())
    else:
        name.append(i)
caseword = ''.join(name)
print(caseword)


# 3 count the occurance of the string 
wordy="kishore"
d = {}
for i in wordy:
    
    if i in d:
        
        d[i]+=1
    else:
        d[i]=1
            
print(d)

# 4 
for i in range(1,51):
    print(i)
    if i %2  == 0:
        print("EVEN :" ,i)
    else:
        print("ODD :" ,i)
        

# 5 
for i in range(1,51):
    if i%3 ==0 and i%5 == 0:
        print(i, "fizz-buzz")
    elif i %3 == 0: 
        print(i , "fizz")
    elif i % 5 == 0:
        print(i , "buzz")

    else: 
        print(i)
        

# 6 
vowels = "aeiou"
word = "accenture"
for i in word: 
    count = 0
    if i in vowels:     
        count+=1
        print(i,count)


# 7 
word = "ga24nbv2k6jg523jg2545lsfwe"
sum = 0
letter = []
for i in word:
    if i.isdigit():
        sum = sum + int(i)
    else: 
        letter.append(i)
print("Sum is :",sum," Characters is : ",letter)

#8 
number = []
for i in range(1,11):
    number.append(i)
print(number)
n = len(number)
sum = 9
for i in range(0,n):
    for j in range(0,n):
        if(number[i]+number[j] == sum):
            print(number[i]," ", number[j])

# 9 
w1 = "add"
w2 = "dad"
if(sorted(w1)==sorted(w2)):
    print("it is anagram" )
else:
    print("it is not an anagram")

#10
a = 11 
for i in range(2,int(a/2)):
    if a%i == 0:
        print("its not a prime")
        break
else:
    print("its a prime")


# 11 
word = (1,2,3,4,5)
#       new = word + (6,)

neww = list(word)
neww.append(6)
print(tuple(neww))

#12 
a = input()
rev = a[::-1]
if a == rev:
    print("it is palindrome " )
else:
    print("it is not palindrome ")

# 13 
num = 11
for i in range(0,21):
    print(num ," x ", i, " = ", num*i)

# 14 

n1 =0
n2 =1 
n =0
while(n<50):
    print(n)
    n = n1 +n2
    n1 = n2
    n2 = n 
    
# 15 
s = []
sentence = "this-is-the-program-a-to-sort-with-hyphen"
for i in sentence.split("-"):
    s.append(i)
s.sort()
print('-'.join(s))

# 16 
li = [1,2,3,3,3,3,4,5]
new = []
for i in li:
    if i not in new:
        new.append(i)
        
print(new)

# 17 
alpha = "abcdefghijklmnopqrstuvwxyz"
word = "IHFJSADFAJSDFsdnff"
for c in alpha:
    if c not in word:
        print("it is not a pangram")
        break;
else: 
    print("it is a pangram")

# 18 
num = []
for i in range(0,5):
    v = int(input("Enter the integer :"))
    num.append(v)
num.sort(reverse = True)
for i in range(0,5):
    if num[i] %2 != 0:
        print(num[i])
        break
   
#19 

r = int(input("Enter the radius in integer"))
area = 3.14*r*r
print(area)   

#20 
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)

print(fact(5))


