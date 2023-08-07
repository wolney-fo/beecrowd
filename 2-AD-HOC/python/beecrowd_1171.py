qty = int(input())

nums = {}

for i in range(qty):
    inp = int(input())

    if inp in nums:
        nums[inp] += 1
    else:
        nums[inp] = 1

for key, value in sorted(nums.items()):
    print('{} aparece {} vez(es)'.format(key, value))