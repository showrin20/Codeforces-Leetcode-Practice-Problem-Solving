k,n,w=[int(i) for i in input().split()]
count=0
for i in range(w):
    p=k*(i+1)
    count=count+p
if count>n:
  print(count-n)
else:
  print(0)
