n=int(input())
for j in range(n):
   p=int(input())
   q=input().upper()
   t=input().upper()
   if q.replace("B","G")==t.replace("B","G"):
     print("Yes")
   else:
     print("No")
