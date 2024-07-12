class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
            
        dic_=dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
        result=list(dic_.keys())[:k]
        return result
