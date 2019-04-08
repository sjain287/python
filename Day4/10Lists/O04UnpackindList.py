nums = list(range(10, 40, 10))
print(nums)
# unpack
# variable count should be equal to List length
f, s, t = nums
print(f'{f}\t{s}\t{t}')

print("_"*50)
nums = list(range(10, 40, 10))
print(nums)
f, s, t = nums

print("_" * 30)
# nums = list(range(10, 41, 5))
# print(nums)
f, s, *t = nums
print(f, s, t)
f, *s, t = nums
print(f, s, t)
*f, s, t = nums
print(f, s, t)
