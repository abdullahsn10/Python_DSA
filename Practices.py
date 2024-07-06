def increasingTriplet(nums):
    count = len(nums)
    if count < 3:
        return False
    
    i, j, k= 0, 1, 2

    while i < j < k:

        if i == count - 2:
            break 

        if k == count:
            j = j+1
            k = j+1
            continue

        if j == count - 1 or j == count:
            i += 1 
            j = i + 1
            k = j + 1
            continue


        if nums[i] < nums[j] and nums[j] < nums[k]:
            return True
        
        else:
            k += 1

    return False





# Test cases
nums = [20,100,10,12,5,13]
print(increasingTriplet(nums))

nums_2 = [2,1,5,0,4,6]
print(increasingTriplet(nums_2))