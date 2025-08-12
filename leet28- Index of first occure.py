arr=[1,0,4,0,3,11,0,9,5,4,0]

for i in range(len(arr)):
    if(arr[i]==0):
        
        for j in range(i+1,len(arr)-1):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
print(arr)