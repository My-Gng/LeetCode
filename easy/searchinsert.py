class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        while i<= len(nums)-1:
            if (nums[i] == target):
                return i
            elif (target<nums[i]):
                return i
            i+=1
        return i



num = [1,3,5,6]
target = 7
search = Solution()
x = search.searchInsert(num, target)
print(x)
