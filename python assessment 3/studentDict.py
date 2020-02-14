
n = int(input("enter the no of students :"))
student = {}
for i in range(1,n+1):
    name = input()
    m = float(input())
    p = float(input())
    c = float(input())
    s= {}
    s['name'] = name
    s['maths'] = m
    s['physics'] = p
    s['chemistry'] = c

    student[i] = s

print(student)
v = input("enter the name to find : ")
for i,j in student.items():
    if v == student[i]['name']:
        print(float((student[i]['maths']+student[i]['physics']+student[i]['chemistry'])/3),"is the average ")


