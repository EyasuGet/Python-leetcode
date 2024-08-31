class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """   
        # if len(nums) == 1:
        #     if nums[0] >= target:
        #         return 0
        #     else:
        #         return 1
        if target in nums:
            return nums.index(target)
        else:
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            if nums[mid] < target:
                return mid + 1
            else:
                return mid
                
