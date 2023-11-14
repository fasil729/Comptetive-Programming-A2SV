class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pref = [0]
        last_ind = {}
        first_ind = {}
        store = set()
        count = 0
        
        for ind, char in enumerate(s):
            if char not in store:
                first_ind[char] = ind
                count += 1
                store.add(char)
            last_ind[char] = ind
            pref.append(count)
        
        ans = 0
        for char in last_ind:
            r = last_ind[char]
            l = first_ind[char]
            ans += len(set(s[l + 1:r]))
            
        return ans