class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        for i in range(len(nums)):
            sanityCheck = nums[i+1:]
            
            if nums[i] in sanityCheck:
                return True
        return False
