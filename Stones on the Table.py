p=int(input())
q=input()
count=0
for i in range(1,len(q)):
  if q[i-1]==q[i]:
    count=count+1
print(count)
