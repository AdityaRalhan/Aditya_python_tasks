# Q)
    # Given an array nums of size n, return the majority element.
    # The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



def majority_element(nums):
    new_nums = nums.sort()
    length_nums = len(nums)
    n = new_nums[length_nums//2]

    if n == new_nums[length_nums//2 - 1] or n == new_nums[length_nums//2 + 1]:
        print(f"{n} appears the most")

    else:
        print("none")

nums = [1,2,3,2,2,3]
# sorted array = [1,2,2,2,3,3]
majority_element(nums)



    


            


    
        





