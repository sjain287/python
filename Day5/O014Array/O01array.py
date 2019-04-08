from array import array
import array as arr
# identical datatypes
# large sequence of numbers
# Mathematical computations

# lists are faster than arrays
# i is for integer
'''
i signed integer
I Unsigned Integer
d double
b signed char
B unsigned char
u py_unicode
h signed short
H unsigned short
l signed long
L unsigned long 
f signed float
F unsigned float
'''
nums = array('i', [1, 2, 3])
print(nums)
print(nums[0])
print(nums[1])
print("_"*50)
nums = array('d', [1.1, 2.1, 3.1])
print(nums)
print(nums[0])
print(nums[-1])
print(nums[1])

print("_" * 50)
array_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums_array = arr.array('i', array_list)
print(nums_array[2:5])
print(nums_array[:-5])
print(nums_array[5:])
print(nums_array[:])

print("_" * 50)
arr1 = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr1)
print("_" * 50)
arr1[0] = 999
print(arr1)
print("_" * 50)
arr1[2:5] = arr.array('i', [11, 22, 33, 44])
print(arr1)

print("_" * 50)
nums = arr.array('i', [11, 22, 33])
print(nums)
nums.append(44)
print(nums)
nums.extend([55, 66, 77, 88])
print(nums)
# ------------------------------------------------------------
print("_" * 50)
odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])
nums = arr.array('i')
nums = odd + even
print(nums)
print("_" * 50)
# del nums[2]
nums.remove(3)
print(nums)
# del nums
nums.pop()
print(nums)
nums.pop(1)
print(nums)
