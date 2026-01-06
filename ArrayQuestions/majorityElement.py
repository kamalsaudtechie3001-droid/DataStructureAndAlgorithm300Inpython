class Solution(object):
    def majorityElementBoyerMoore(self ,nums):
        n = len(nums)  # Calculate the length of the array.
        count = 0
        candidate = nums[0]
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
    def isMajorityElement(self, nums, target):
        n = len(nums)
        # Find the majority element using Boyer Moore voting algorithm.
        candidate = self.majorityElementBoyerMoore(nums)
        if candidate == target and nums.count(target) > n//2:
            return True
        
        return False
# Create a constructor to call the function outside the class   
sol = Solution()
nums = [2,4,5,5,5,5,5,6,6]
ans = sol.isMajorityElement(nums,target=5)
print(ans)