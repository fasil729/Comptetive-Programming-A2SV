class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        """
        
        # intialization
        ans = []
        subset = []
        n = len(nums)
       
        
        def recurse(ind):
            ans.append(subset.copy())
            # base case
            if ind == n:
                return None
            
            # recursive relation
            for i in range(ind, n):
                subset.append(nums[i])
                recurse(i + 1)
                subset.pop()
            
            
            return None
        
        recurse(0)
        
        return ans
        
        
       