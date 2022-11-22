string1="abcdefghijklmnopqrstuvwxyz"
t=int(input())
for j in range(t):
  n=int(input())
  list1=[]
  s=input()
  for i in range(len(s)):
    if s[i] in string1:
      list1.append(string1.index(s[i])+1)
  print(max(list1))
