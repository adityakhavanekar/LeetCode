nums = [1,2,3,1]
dictn = {}

for i in nums:
    if i in dictn:
        dictn[i]+=1
    else:
        dictn[i]=1

print(dictn)

flag = 0
for i in dictn:
    if dictn[i]>1:
        flag = 1
        break
    else:
        continue
    
if flag == 0:
    print("false")
else:
    print("true")

    
