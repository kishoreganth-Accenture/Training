import math
t = int(input("enter the number of rrational numbers needed to multiply :"))
product = 1
num = 1
den = 1
for i in range(t):
    a = int(input())
    b = int(input())
    product= product * a/b

print(product.as_integer_ratio())