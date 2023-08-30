class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def solve(arr,k,n,ans):
            if n==1:
                ans+=str(arr[0])
                return ans
            f=factorial(n-1)
            ind=k//f
            ans+=str(arr[ind])
            arr.pop(ind)
            k%=f
            return solve(arr,k,n-1,ans)
        
        arr=[i for i in range(1,n+1)]
        k-=1
        ans=''
        return solve(arr,k,n,ans)
        