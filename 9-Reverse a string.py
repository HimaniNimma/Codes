#Reverse a string
name=input("Enter string")
m=len(name)
empty=""
for i in range (m-1,-1,-1):
    print(name[i])
    empty=empty+name[i]
print(empty)
 
