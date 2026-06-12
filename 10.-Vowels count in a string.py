#Vowels count in a string
h=input("enter string")
vowels=0
for i in h:
    if i in "aeiouAEIOU":
        vowels=+1
print(vowels)
