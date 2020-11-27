#二分搜尋法
nums = [3,6,9,15,22,45,52,68,77,84,96,108,118]
find = 45
low = 0
high = len(nums)-1
i=0
while low <= high:
    i+=1
    mid = (high+low)//2
    if nums[mid] > find:
        high = mid - 1
    elif nums[mid] < find:
        low = mid + 1
    else:
        break
print(mid,nums[mid],i)