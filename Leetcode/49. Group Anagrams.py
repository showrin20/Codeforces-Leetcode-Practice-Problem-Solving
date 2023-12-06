class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            an = "".join(sorted(i))
            if an not in d:
                d[an] = [i]
            else:
                d[an].append(i)
        return d.values()
