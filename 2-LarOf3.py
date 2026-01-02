#largest of 3 nums
h=int(input("Enter n1"))
m=int(input("Enter n2"))
k=int(input("Enter n3"))
if(h>m):
    if(h>k):
        print(h)
    else:
        print(k)
elif(m>k):
    print(m)
else:
    print(k)
