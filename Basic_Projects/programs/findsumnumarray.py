
from pickle import FALSE, TRUE


a = {1,8,9,3,7,5,7,4,3}

sum = 10
found=FALSE
for i in a:
    j=i+1
    if sum > i:
        rem = sum-i
        for j in a:
            if rem==j:
                print("True")
                found = TRUE
                print("Found sum at location : ",i)
                print("Found sum at location : ",j)
    if found==TRUE:
        break
if found==FALSE:
    print("Sorry we coudn't found the expected")

        
            

    

