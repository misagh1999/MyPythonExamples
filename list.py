list1=[]
a=1
for a in range(5,10):
    list1.append(a)
    a+=1
for b in list1:
    print b,
print
list2=list1[1:6]
for c in list2:
    print c,
print
for k in list2:
    list2[k]=list2[k]*5
for d in list2:
    print d,
