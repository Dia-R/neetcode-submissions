class Solution:
    def isPalindrome(self, s: str) -> bool:
        stackForward = []
        stackBackward = []
        
        for i in range(len(s)):
            if s[i].isalnum():  
                letter = s[i].lower()
                stackForward.append(letter)
        
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                letter = s[i].lower()
                stackBackward.append(letter)
        return stackForward == stackBackward
