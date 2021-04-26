n,m=map(int,input().split())
k=[]
for i in range(n):
    l=input().split()
    k.append(l)
s=[]
for i in range(m):
    for j in range(n):
        if k[j][i].isalnum():
            s.append(k[j][i])
s1=''.join(s)
print(s1)
        
    
