List = ["Canada","Brazil","Japan","India","Norway"]
for i in List:
    if "Japan" in i:
        print("Tokyo")
    else:
        print(i)

for i in range(5):  #End Value
    print(i)

for i in range(1,10):  #Start,End
    print(i)

for i in range(0,20,2):  #start, end,inc/dec
    print(i)

num = int(input("Enter Your Number")) #4
temp = 0
for i in range(2,num):
    if num % i == 0:
        temp += 1
        break


if temp > 0:
    print("Composite")
else:
    print("Prime")   