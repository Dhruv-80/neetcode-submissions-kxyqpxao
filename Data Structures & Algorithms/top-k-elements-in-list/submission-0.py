class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap = {}
        # for num in nums:
        #     hashmap.get(0,num)+1
        hashmap = Counter(nums)
        return [num for num, count in hashmap.most_common(k)]
        
        