class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1, nums2 = set(nums1), set(nums2)

        ignore_values = nums1.intersection(nums2)

        answer: List[List[int]] = [[],[]]

        for n in nums1:
            if n not in ignore_values:
                answer[0].append(n)

        for n in nums2:
            if n not in ignore_values:
                answer[1].append(n)


        return answer