# Big O Notation:
# Indexing: O(1)
# Searching: O(n)
# Traversing: O(n)
# Inserting: O(n) it will shift all elements
# Deleting: O(n) it will shift all element
# Array is stored in memory as a contigous block
# for indexing, arr[i] = base_address + i*sizeof(int)
# Arrays can be static or dynamic arrays

# ---------------------------------------------
# nums = [1, 2, 3, 4, 5, 6]
 
# # get every single triplet
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         for k in range(j+1, len(nums)):
#             print(nums[i], nums[j], nums[k])
# -------------------------------------------
# Binary search
# nums = [10, 20, 30, 
#         40, 50, 60,
#          70, 80, 90, 110, 120]
# target = 40
# l, r = 0, len(nums) -1
# while l <= r:
#     m = (l + r) // 2
#     if target > nums[m]:
#         l= m+1
#     elif target < nums[m]:
#         r = m-1
#     else:
#         print(m)
#         break
# --------------------
# nums = [1, 2, 3, 4]
# print(nums.pop(2))
# print(nums)
# -----------------------
nums = [13, 2, 4, 7, 11, 15, 16, 22, 28, 33, 32, 31]
for num in list(filter(lambda number : number % 2 == 0, nums)):
    print(num)

# if flowerbed.count(0) < n:
#             return False
        
#         if not n:
#             return True
        
#         while n:
#             if not flowerbed.count(0):
#                 break
#             zero_index = flowerbed.index(0)
#             after_zero = zero_index + 1
#             before_zero = zero_index - 1
#             # end of flowerbed
#             if after_zero >= len(flowerbed):
#                 if flowerbed[before_zero]:
#                     return False
#                 else:
#                     flowerbed[zero_index] =1
#                     n -=1
#                     continue
#             #start of flowerbed
#             if before_zero < 0:
#                 if flowerbed[after_zero] == 1:
#                     flowerbed = flowerbed[zero_index + 1:]
#                     continue
#                 else: 
#                     flowerbed[zero_index] = 1
#                     n -= 1
#                     continue
#             # any place between start and end
#             if flowerbed[before_zero] or flowerbed[after_zero]:
#                 flowerbed = flowerbed[zero_index + 1:]
#             else:
#                 flowerbed[zero_index] = 1
#                 n -= 1
            
#         if n:
#             return False
#         return True

# ------------------------------
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if not n: 
#             return True
#         if n > flowerbed.count(0):
#             return False

#         can_place = list()


#         while flowerbed.count(0):
#             zero_index = flowerbed.index(0)
#             bed_len = len(flowerbed)

#             if len(flowerbed) == 1:
#                 can_place.append(True)
#                 break
#             else:
#                     # start
#                 if zero_index == 0:
#                     if flowerbed[zero_index + 1]:
#                         can_place.append(False)
#                     else:
#                         can_place.append(True)
#                         flowerbed[zero_index] = 1
#                         continue
                
#                 elif zero_index == bed_len - 1:
#                     if flowerbed[zero_index - 1]:
#                         can_place.append(False)
#                     else:
#                         can_place.append(True)
#                         flowerbed[zero_index] = 1
#                         continue
#                 else:
#                     #between
#                     if flowerbed[zero_index + 1] or flowerbed[zero_index - 1]:
#                         can_place.append(False)
#                     else:
#                         can_place.append(True)
#                         flowerbed[zero_index] = 1
#                         continue
#                 flowerbed = flowerbed[zero_index+1:]
        
#         if can_place.count(True) >= n:
#             return True
        
#         return False

        
                


            
        

