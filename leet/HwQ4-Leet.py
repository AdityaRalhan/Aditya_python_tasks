# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


nums = [2,3,4,5]
target = 9
check = 0

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):

        if target == nums[i]+ nums[j]:
            print(f'{i} and {j}')
            

        else:
           pass
    

