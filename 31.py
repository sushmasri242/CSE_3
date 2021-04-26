t=int(input())
for i in range(t):
    s=input()
    l1=[]
    l2=[]
    for l in s:
        if l.lower()=='i':
            l1.append(l)
        else:
            l2.append(l)
    c=0
    for k,p in zip(l1,l2):
        if k=='I' and p=='O':
            c+=1
    print('Case #'+str(i)+':',c)
