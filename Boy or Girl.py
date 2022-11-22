p=input()
q=""
for i in p:
  if i not in q:
    q+=i
if len(q)%2==0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
