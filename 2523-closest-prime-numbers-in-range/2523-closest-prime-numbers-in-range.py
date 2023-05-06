class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        arr = self.seive(right)
        primes = [i for i in range(left, right + 1) if arr[i]]
        if len(primes) < 2:
            return -1, -1
        ans = (-inf, 0)
        last = primes[0]
        for ind in range(1, len(primes)):
            if ans[1] - ans[0] > primes[ind] - last:
                ans = (last, primes[ind])
            last = primes[ind]
        return ans
        
    def seive(self, n):
        is_prime = [True for i in range(n + 1)]
        is_prime[0] = is_prime[1] = False


        i = 2
        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1

        return is_prime

        
        
        
        
        
        
        
        
        
        
        
        
    
        