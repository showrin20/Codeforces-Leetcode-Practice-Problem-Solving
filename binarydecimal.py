n=int(input())
for i in range(n):
    p=input()
    lis=[]
    for i in p:
        lis.append(int(i))
    print(max(lis))
