class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        temp = []
        freq = 0
        for word in words:
            if freq + len(temp) + len(word) <= maxWidth:
                temp.append(word)
                freq += len(word)
                continue
                
            
            extra = maxWidth - (freq + len(temp) - 1)
            if len(temp) == 1:
                res.append(" ".join(temp) + extra * " ")
                temp = [word]
                freq = len(word)
                continue

            slot = len(temp) - 1
            div, mod = divmod(extra, slot)
            ind = 1
            s = ""
            for ind, w in enumerate(temp):
                if mod > 0:
                    rem = 1
                else:
                    rem = 0
                s += w
                if extra > 0:
                    pad = " " * (div + rem)
                    s += pad
                    mod -= 1
                    extra -= len(pad)
                if ind != len(temp) - 1:
                    s += " "
                
                
            res.append(s)
            temp = [word]
            freq = len(word)
        
        pad = " " * (maxWidth - (freq + len(temp) - 1))
        res.append(" ".join(temp) + pad)
        return res
                
            
            
        