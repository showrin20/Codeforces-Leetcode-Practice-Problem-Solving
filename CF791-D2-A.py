p,q=[int(i) for i in input().split()]
count=0
while p<=q:
  p=p*3
  q=q*2
  count=count+1
print(count)
