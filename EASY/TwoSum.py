def twosum(nums, target):
    count = len(nums)
    x = 0
    y = 0
    for x in range(count):
        for y in range(x + 1, count):
            if (target == nums[x] + nums[y]):
                return [x, y]

nums = [3, 2, 4]
target = 6
print(twosum(nums, target))
'''
def twoSum(nums, target):
    i = 0
    q = 0
    for i in range(0, len(nums)):
        m = target - nums[i]
        if m in nums:
            q = nums.index(m)
            if q != i:
                break
    return [i, q]
nums = [3, 2, 4]
target = 6
twoSum(nums, target)
'''