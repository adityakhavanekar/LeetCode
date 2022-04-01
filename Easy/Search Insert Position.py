class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            print(nums.index(target))
        else:
            if nums[-1]<target:
                nums.append(target)
            else:
                for i in nums:
                    if i>target:
                        nums.insert(nums.index(i),target)
                        break
        return nums.index(target)
