n=int(input())
x=0
for i in range(n):
  q=input()
  if "++" in q:
    x=x+1
  else:
    x=x-1
print(x)
