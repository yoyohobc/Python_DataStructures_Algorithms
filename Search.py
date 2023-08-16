#二分搜尋法O(log n)
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

#選擇排序法O(n^2)
Numbers = [41,33,17,80,61,5,55]
length = len(Numbers)

for i in range(length):
    min_index = i
    for j in range(i+1,length):
        if Numbers[min_index] > Numbers[j]:
            min_index=j

    Numbers[i],Numbers[min_index] = Numbers[min_index],Numbers[i]

print(Numbers)
#插入排序法O(n^2)
Numbers = [41,33,17,80,61,5,55]
length = len(Numbers)
for i in range(1, length):
    position = i
    value = Numbers[i]
    print('\n'+str(i))
    while position > 0 and Numbers[position-1] > Numbers[position]:
        print('P:',position)
        Numbers[position], Numbers[position-1] = Numbers[position-1], Numbers[position]
        position -= 1
        print(Numbers)
print(Numbers)
