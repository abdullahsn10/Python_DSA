def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
             elements[j+1] = elements[j]
             j -= 1
        elements[j+1] = anchor

nums = [7, 11, 2, 3, 5, 20, 1, 19]
insertion_sort(nums)
print(nums)