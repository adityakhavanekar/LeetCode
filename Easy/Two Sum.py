class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = 0
        ans = []
        if len(nums)>=2:
            for i in range(0,len(nums)):
                    for j in range(i+1,len(nums)):
                        if nums[i]+nums[j] == target:
                            ans.append(i)
                            ans.append(j)
                            flag = 1
                            break
                        else:
                            continue
                    if flag == 0:
                        continue
                    else:
                        break
        return ans

    