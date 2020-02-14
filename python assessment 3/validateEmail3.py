import re
email = []
n = int(input("enter the no of emails : "))
for i in range(3):
    a = input()
    email.append(a)

words= " ".join(email)
print(words)
p = re.findall(r"\w+\@.\w+\..{50}",words)
print(p)

