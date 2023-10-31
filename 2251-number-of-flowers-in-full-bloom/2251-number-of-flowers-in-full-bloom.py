class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        arr = []
        for start, end in flowers:
            arr.append(start)
            arr.append(end + 1)
        arr.append(0)
        arr = list(set(arr))
        arr.sort()
        n = len(arr)
        
        def get_index(num):
            l, r = 0, len(arr) - 1
            
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] <= num:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return l
        
        pref = [0] * (n + 1)
        for start, end in flowers:
            i = get_index(start) - 1
            j = get_index(end) - 1
            pref[i] += 1
            if j < n - 1:
                pref[j + 1] -= 1
        print(pref)
        for i in range(1, n + 1):
            pref[i] += pref[i - 1]
        
        print(pref)
        print(arr)
        
        ans = []
        for p in people:
            ind = get_index(p) - 1
            ans.append(pref[ind])
        return ans
        