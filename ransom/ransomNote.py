from collections import defaultdict
class Solution(object):
    def letter_frequency(self,sentence):
        frequencies = defaultdict(int)
        if sentence is None:
            frequencies["len"] = 0
        else:
            for letter in sentence:
                frequencies[letter] += 1
        return frequencies

    def canConstruct(self, ransomNote, magazine):
        self.flag = True
        ransomNote_frequency  = self.letter_frequency(ransomNote)
        magazine_frequency = self.letter_frequency(magazine)
        for letter, frequency in ransomNote_frequency.items():
            if magazine_frequency[letter] and magazine_frequency[letter] >= frequency:
                self.flag = True
                continue
            else:
                self.flag = False
                break
        return self.flag

        
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        