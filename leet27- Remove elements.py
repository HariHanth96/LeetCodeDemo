nums = [2]
val = 3

nums.sort()

print(nums)
i_s=i_e=0
for i in range(len(nums)):
    if(nums[i]==val):
        i_s=i
        break
for j in range(len(nums)-1,-1,-1):
    if(nums[j]==val):
        i_e=j
        break
for i in range(i_s,i_e+1):
    try:
        nums[i]=nums[i+(i_e-i_s+1)]
    except:
        break
print(nums)
print( i_e-i_s+1)
