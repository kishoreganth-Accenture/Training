import mysql.connector
import json
import collections


mydb = mysql.connector.connect(host ="localhost",user ="root",password = "root",db = "pythonconnect")

cursor = mydb.cursor()
cursor.execute("drop table employer")
sql = "create table if not exists employer(id int,name varchar(30),phone int, salary int)"
cursor.execute(sql)
cursor.execute("desc employer")
print(cursor.fetchall())

f = open("data.csv")
rows = f.readlines()

# isql = "insert into employee(id,name,phone,salary) values(idd,namee,phonee,salaryy)"

for i in rows:
    a = i.split(",")
#     # print(a)
#     # idd = a[0]
#     # namee = a[1]
#     # phonee = a[2]
#     # salaryy = a[3]
#     # val = (int(idd),namee,int(phonee),int(salaryy))
#     # print(idd,namee,phonee,salaryy)
    cursor.execute("insert into employer(id,name,phone,salary) values(%s,%s,%s,%s)",a)

mydb.commit()
cursor.execute("select * from employer")
data = cursor.fetchall()
# print(json.dumps({'employee':data},indent=4))
#
# print(cursor.next())
# print(json.dumps(cursor.next(),indent=4))
# print(cursor.next())
count = 0
objectfiles = ["employer1.json","employer2.json","employer3.json","employer4.json"]
for r in data:
    object = []
    print(r)
    d = collections.OrderedDict()
    d['id'] = r[0]
    d['name'] = r[1]
    d['phone'] = r[2]
    d['salary'] = r[3]
    object.append(d)
    j = json.dumps(object,indent=4)

    f = open(objectfiles[count],"w")
    count += 1
    f.write(j)

mydb.close()
