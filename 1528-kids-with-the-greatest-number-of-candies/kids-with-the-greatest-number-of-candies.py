class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx=max(candies)
        result=[]
        for i in candies:
            if extraCandies+i>=maxx:
                result.append(True)
            else:
                result.append(False)
        return result