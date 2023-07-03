class FreqWord(object):
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for w in words:
            freq[w] += 1
       
        heap = []
        for word, f in freq.items():
            
            if len(heap) == k:
                heapq.heappushpop(heap, FreqWord(f, word))
            else:
                heapq.heappush(heap, FreqWord(f, word))
        
        
        
        ans = []
        while heap:
            ans.append(heapq.heappop(heap).word)
        
        return ans[::-1]
       
        
   

        