nums = [2,3,4,5]
target = 9
check = 0

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):

        if target == nums[i]+ nums[j]:
            print(f'{i} and {j}')
            

        else:
           pass
    

