l=input().split()
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(len(l1),end=' ')
for i in l1:
    print(l.count(i),end='')
    
