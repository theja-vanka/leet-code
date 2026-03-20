class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        l1: int = len(nums1)
        l2: int = len(nums2)

        if l1 < l2:
            nums1, nums2 = nums2, nums1
        
        hashmap: dict = {}
        result: list = []

        for n in nums1:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        
        for n in nums2:
            if n in hashmap and hashmap[n] > 0:
                hashmap[n] -= 1
                result.append(n)
        
        return result
        

