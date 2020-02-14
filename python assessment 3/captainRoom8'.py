k = int(input("enter the size of the each group "))

sizeSatisfied = []

peopleRoom = "1236544253616532412514368431562"
if len(peopleRoom)%k==0 :
    print("there is no room for captain")
else:
    rooms = int(len(peopleRoom)/k)
    print(rooms)
    for i in peopleRoom:

        if peopleRoom.count(i) == k:
            if i not in sizeSatisfied:
                sizeSatisfied.append(i)

print(sizeSatisfied)

for j in peopleRoom:
    if j not in sizeSatisfied:
        print(j, "is the captain room ")


