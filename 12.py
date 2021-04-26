a=input()
b=input()
res=""
for i in a:
    temp=ord(i)-65
    res+=chr(((temp+5)%26)+65)
flag=True
for i in b:
    if i not in res:
        flag=False
        break
if flag:
    print("Yes")
else:
    print("No")
