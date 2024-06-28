boysname=input("Enter the boy's name: ")
girlsname=input("Enter the girl's name: ")
flames=['Friendship','Love','Affair','Marriage','Enemy','Sister']
boysnamelst=[]
for i in boysname:
    boysnamelst.append(i)
girlsnamelst=[]
for i in girlsname:
    girlsnamelst.append(i)
for i in boysnamelst:
    for j in girlsnamelst:
        if i==j:
            boysnamelst.remove(i)
            girlsnamelst.remove(i)
print(boysnamelst)
print(girlsnamelst)
length=len(boysnamelst+girlsnamelst)
lengthofflames=len(flames)
for i in range(1,6):
    cutnumber=length%lengthofflames
    del flames[cutnumber]
    lengthofflames-=1





