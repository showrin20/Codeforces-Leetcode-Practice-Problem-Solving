n=int(input())
for j in range(n):
  list1=[int(i) for i in input().split()[:3]]
  list1.sort()
  if list1[0]+list1[1]==list1[2]:
    print("Yes")
  else:
    print("No")
