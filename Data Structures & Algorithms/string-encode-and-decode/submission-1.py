class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ''
        for string in strs:
            output += (str(string) + '~')
        return(str(output))

    def decode(self, s: str) -> List[str]:
        word = ''
        output = []
        for i in range(len(s)):
            if s[i] != '~':
                word += (s[i])
            else:
                word = str(word)
                output.append(word)
                word =''
        
        return output

