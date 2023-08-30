class Solution:
    def jump(self, nums: List[int]) -> int:
        #print(nums)
        L=len(nums)
        if L==1:
            return 0
        steps=[0]
        for i in range(nums[0]):
            steps.append(1)
        for index in range(1,L):
            len_steps=len(steps)
            if len_steps >= nums[index]+index+1:
                index += 1
            elif len_steps < nums[index]+index+1:
                for j in range(nums[index]+index-len_steps+1):
                    #print(index-1,steps[index-1])
                    steps.append(steps[index]+1)
            #print(steps)
        return steps[L-1]
        