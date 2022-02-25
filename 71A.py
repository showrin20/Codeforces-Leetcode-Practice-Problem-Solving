n=int(input())
for i in range(0,n):
    word=input()
    word_lenth=len(word)
    middle_word=str(word_lenth-2)
    if word_lenth>10:
        print(word[0]+middle_word+word[len(word)-1])
    else:
        print(word)