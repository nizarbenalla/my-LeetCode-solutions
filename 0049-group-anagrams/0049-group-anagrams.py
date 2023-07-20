class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or strs == [""]: return [[""]]
        d = defaultdict(list)
        for i in strs:
            l = [0]*26
            for letter in i :
                l[ord(letter)-97]+=1
            d[tuple(l)].append(i)
        return [d[j] for j in d]