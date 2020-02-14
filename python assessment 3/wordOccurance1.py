
n = int(input("Enter the number of words :"))
words = []
print(n)
for i in range(n):
    a = input()
    words.append(a)

# print(words)
setWords = set(words)
print(len(setWords))
for w in setWords:
    print(words.count(w),end = " ")


