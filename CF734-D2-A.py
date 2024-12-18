
n=input().upper()
p=input()
countA=0
countB=0
for i in p:
    if i=="A":
        countA=countA+1
    else:
        countB = countB + 1
if countA>countB:
    print("Anton")
elif countA==countB:
    print("Friendship")
else:
    print("Danik")
