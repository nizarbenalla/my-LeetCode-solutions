class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or strs == [""]: return [[""]]
        d = defaultdict(list)
        for i in strs:
            l = [0]*26
            for letter in i :
                l[ord(letter)-ord('a')]+=1
            key = "".join(str(i+ord('a'))+str(l[i]) for i in range(len(l)))
            d[key].append(i)
        output =[]
        for j in d:
            output.append(d[j])
        return output