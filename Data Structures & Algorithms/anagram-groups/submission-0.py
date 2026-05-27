from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strdict = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            strdict[sortedS].append(s)
        return list(strdict.values())            

