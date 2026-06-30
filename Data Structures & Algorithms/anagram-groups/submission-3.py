class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} #key type will be sorted string, value is list
        for string in strs:
            strsSorted = ''.join(sorted(string))

            if strsSorted in hashMap:
                hashMap[strsSorted].append(string)
            else:
                hashMap[strsSorted] = [string]
             
        output = hashMap.values()
        return(list(output))
