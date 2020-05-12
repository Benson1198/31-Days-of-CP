class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if mid%2==0:
                # if mid is even 
                if nums[mid]==nums[mid+1]:
                    left=mid+2
                else:
                    right=mid
            else:
                # mid is odd
                if nums[mid]==nums[mid-1]:
                    left=mid+1
                else:
                    right=mid
        return nums[left]
    