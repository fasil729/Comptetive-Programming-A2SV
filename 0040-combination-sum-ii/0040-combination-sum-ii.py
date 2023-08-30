class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        Len = len(candidates)
        C = sorted(candidates)
        
        def rec(List,ind):
            s = sum(List)
            if s == target and List not in ret: 
                ret.append(List)
            elif s < target:
                for i in range(ind,Len): 
                    if i > ind and C[i] == C[i-1]:  
                        continue
                    # if s + sum(C[i:]) < target:  
                    #     break
                    rec(List+[C[i]],i+1)
        
        rec([],0)
        return ret
        