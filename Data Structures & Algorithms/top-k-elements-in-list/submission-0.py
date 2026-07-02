class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for i in nums:
            if i in(count.keys()):
                count[i] += 1
            else:
                count[i] = 1
                
                
            print(count)
        for i in range(k):

            v = (max(count.values()))
            print(v)
            k = [key for key, value in count.items() if value == v]
            print(k)
            result.append(k[0])
            count.pop(k[0])
            print(count)
            print(result)
        return result
            