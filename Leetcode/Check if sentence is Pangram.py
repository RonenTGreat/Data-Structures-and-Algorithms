# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set();
        for letter in sentence:
            letters.add(letter)
        return len(letters) == 26


sentence_1 = "thequickbrownfoxjumpsoverthelazydog"
test_1 = Solution()
print(test_1.checkIfPangram(sentence_1))

sentence_2 = "leetcode"
test_2 = Solution()
print(test_2.checkIfPangram(sentence_2))
