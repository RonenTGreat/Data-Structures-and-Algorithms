class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        return len(words[len(words) - 1])
