class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()
        for letter in sentence:
            letters.add(letter)
        return len(letters) == 26
