class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
        new_nums = [x for x in nums if x is not None]
        nums[:] = new_nums
        return len(nums)

object = Solution()
num =  [3, 2, 1, 3]
val = 2
x = object.removeElement(num, val)
print(x)