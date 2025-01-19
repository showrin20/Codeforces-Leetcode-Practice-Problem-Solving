class Solution:
    def countBits(self, n: int) -> List[int]:
        c=[]
        for i in range(n+1):
             c.append(bin(i).count("1"))
        return c