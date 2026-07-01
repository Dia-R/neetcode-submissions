class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringCount = len(strs)
        anagramMap = {}

        for i in range(stringCount):
            stringMap = [0]*26
            for k in range(len(strs[i])):
                curCharPos = ord(strs[i][k]) - 97
                stringMap[curCharPos] += 1
            charCount = ",".join(str(c) for c in stringMap) 

            if charCount in anagramMap:
                anagramMap.get(charCount).append(strs[i])
            else:
                anagramMap[charCount] = [strs[i]]
        
        return(list(anagramMap.values()))
        
    

                
        