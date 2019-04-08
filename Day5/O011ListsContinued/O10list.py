nums = [1, 8, 10, 4, 5]
print(nums)
print(id(nums))
print("_" * 50)

# sorting a list at same memory
nums.sort()
print(nums)
print(id(nums))
print("_" * 50)

nums.sort(reverse=True)
print(nums)
print(id(nums))
print("_" * 50)

# sorting a list at different memory
nums = [1, 8, 10, 4, 5]
print(nums)
print(sorted(nums))
print("_" * 50)

print(nums)
print(sorted(nums, reverse=True))
print("_" * 50)
