class Solution:
    def wordSubsets(self, A, B):
        counter_b = defaultdict(int)
        ans = []
        for b in B:
            for char, freq in Counter(b).items():
                counter_b[char] = max(counter_b[char], freq)
        
        
        
        for a in A:
            if self.check_subset(a, counter_b):
                    ans.append(a)
                    
        return ans
    
    def check_subset(self, a, count_b):
        count_a = Counter(a)
        for k in count_b:
            if not k in count_a:
                return False
            if k in count_a and count_b[k] > count_a[k]:
                return False
        return True
        
                