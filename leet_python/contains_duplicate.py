
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice 
# in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums):
    
        #  USING SORT FUNCTION <-----
        # nums.sort()
        # print(nums)
        # for i in range(len(nums)-1):
        #     print(i)
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False

        #  USING HASH TABLE / CACHE  <----
        # hash = {}

        # for i in nums:
        
        #     if i in hash:
        #         return True
        #     else:
        #         hash[i] = 0
            
        #     print(hash)
        # return False



    # ONE LINE TERNARY
        return True if len(set(nums)) < len(nums) else False


test1 = Solution()
print(test1.containsDuplicate([1,2,3,1]))