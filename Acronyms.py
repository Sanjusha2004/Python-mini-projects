user=input("Enter the word")
s=user.split()
a=""
for i in s:
    a+=str(i[0]).upper()
print(a)

