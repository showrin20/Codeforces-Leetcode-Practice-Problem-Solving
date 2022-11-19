n=int(input())
count=0
for i in range(n):
  p,q= [int(item) for item in input().split()]
  if q-p>=2:
      count=count+1
print(count)
