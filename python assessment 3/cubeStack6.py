n = int(input("enter the number of cube stack : "))
cubes = []

for i in range(n):
    a = int(input())
    cubes.append(a)
print(cubes)
cube1 = []
print("cube1")
for c1 in range(cubes[0]):
    a = int(input(" "))
    cube1.append(a)
print("cube2")
cube2=[]
for c2 in range(cubes[1]):
    b = int(input(" "))
    cube2.append(b)


# cube1 = [4, 3, 2, 1, 3, 4]
# cube2 = [1, 3, 2]

print(cube1)
j = len(cube1)
for i in range(len(cube1)//2):
    j -= 1
    # print(cube1[i],cube1[j])
    if cube1[i] >= cube1[j]:
        continue
    else:
        print("no")
        break
else:
    print("yes")

#case 2
print(cube2)
j2 = len(cube2)
for i2 in range(len(cube2) // 2):
    j2 -= 1
    # print(cube2[i2], cube2[j2])
    if cube2[i2] >= cube2[j2]:
        continue
    else:
        print("no")
        break
else:
    print("yes")




