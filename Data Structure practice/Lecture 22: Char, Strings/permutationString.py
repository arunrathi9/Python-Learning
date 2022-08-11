# LeetCode problem - permutation of string

class Solution:
    def checkCount(self,c1, c2):
        for i in range(len(c1)):
            if c1[i] != c2[i]:
                return False
        return True
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0]*26
        window_size = len(s1)
        for i in range(window_size):
            index = ord(s1[i]) - ord('a')
            count1[index] += 1
    
        # traverse the s2 string

        i = 0
        count2 = [0]*26
        # first window
        while(i<window_size and i < len(s2)):
            index = ord(s2[i]) - ord('a')
            count2[index] += 1
            i += 1

        if self.checkCount(count1, count2):
            return True

        # traverse remaining s2 string
        while(i<len(s2)):
            index = ord(s2[i]) - ord('a')
            count2[index] += 1

            index = ord(s2[i-window_size])-ord('a')
            count2[index] -= 1

            i += 1
            if self.checkCount(count1, count2):
                return True    

        return False

s = Solution()
print(s.checkInclusion('ab', 'eidbaooo'))
print(s.checkInclusion('ab', 'eidboaoo'))
print(s.checkInclusion('ab', 'a'))
print(s.checkInclusion('ab', 'ba'))