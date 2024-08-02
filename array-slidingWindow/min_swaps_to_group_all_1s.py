class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        totalOnes = nums.count(1)
        l = 0
        windowOnes = maxWindowOnes = 0
        for r in range(2 * n):
            if nums[r % n]:
                windowOnes += 1
            if r - l + 1 > totalOnes:
                windowOnes -= nums[l % n]
                l += 1
            maxWindowOnes = max(windowOnes, maxWindowOnes)
        return totalOnes - maxWindowOnes
