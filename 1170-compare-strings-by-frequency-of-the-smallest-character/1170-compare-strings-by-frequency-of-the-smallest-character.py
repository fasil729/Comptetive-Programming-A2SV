class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def fr(word):
            f = 0
            mini = "z"
            for char in word:
                if char < mini:
                    f = 0
                    mini = char
                if char == mini:
                    f += 1
        
            return f
        
        freq = []
        for word in words:
            f = fr(word)
            freq.append(f)
        freq.sort()
        def binary(val):
            l, r = 0, len(freq) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if freq[mid] <= val:
                    l = mid + 1
                else:
                    r = mid - 1
            return len(freq) - l
        ans = []
        for q in queries:
            val = fr(q)
            ans.append(binary(val))
        return ans
            
                