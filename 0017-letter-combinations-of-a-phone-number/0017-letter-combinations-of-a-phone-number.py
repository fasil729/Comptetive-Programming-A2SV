class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        
        
        def backtrack(index, mapp, res, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return res
            digit = digits[index]
            for letter in mapp[digit]:
                path.append(letter)
                backtrack(index + 1, mapp, res, path)
                path.pop()
            
            return res
        return backtrack(0, mapp, [], []) if digits else []
        
        
            
        
        