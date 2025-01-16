class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        st = list(s)  
        l = 0  
        temp = []  

        for i in range(len(s) - 1, -1, -1):
            if s[i] in vowels:
                temp.append(s[i])
        
        for i in range(len(s)):
            if s[i] in vowels:
                st[i] = temp[l]
                l += 1
        
        return ''.join(st) 
