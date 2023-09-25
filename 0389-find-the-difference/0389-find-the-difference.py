class Solution:
    def findTheDifference1(self, s: str, t: str) -> str:
        # hash table
        count_t = Counter(t)
        count_s = Counter(s)
        for char in count_t:
            if char not in count_s or count_s[char] != count_t[char]:
                return char
    def findTheDifference(self, s: str, t: str) -> str:
        # bit manuplation
        bit_map = 0
        for char in s + t:
            bit_map ^= ord(char)
        return chr(bit_map)
            

        