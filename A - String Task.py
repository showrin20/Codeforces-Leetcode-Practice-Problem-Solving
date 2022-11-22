q="aoyeui"
c=""
p=input().lower()
for i in p:
  if i not in q:
    c=c+"."+i
print(c)
