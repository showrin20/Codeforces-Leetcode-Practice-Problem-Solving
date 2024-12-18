n,h=[int(i) for i in input().split()]
lst=[int(i) for i in input().split()[:n]]
min=0
for i in lst:
    if i>h:
        min=min+2
    else:
        min=min+1
print(min)
