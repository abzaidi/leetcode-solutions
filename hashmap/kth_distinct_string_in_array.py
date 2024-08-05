class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        countDict = {}
        for s in arr:
            countDict[s] = countDict.get(s, 0) + 1
        
        distinct = [s for s, count in countDict.items() if count == 1]
        if k <= len(distinct):
            return distinct[k - 1]
        else:
            return ""
