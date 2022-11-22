n=int(input())
for j in range(n):
  list1=[int(i) for i in input().split()[:3]]
  list1.sort()
  print(list1[1])
