import random
import string


def string_generator(size=9, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for str in range(9))

thedepartment = input("What is the name of your department.") 
    
for str in thedepartment:
    
    if thedepartment == "Marketing" or thedepartment.lower() == "marketing":
        print("TheDepartment verification is processing")
        break
    
    elif thedepartment == "FinOps" or thedepartment.lower() == "finops":
        print("TheDepartment verification is processing")
        break
    
    elif thedepartment == "Accounting" or thedepartment.lower() == "accounting":
        print("TheDepartment verification is processing")
        break
    
    else:
        print(": The Department verification failed. Please re enter the correct department name.")
        exit()
        
instances = int(input("How many EC2 instances with unique names.: "))
    
if instances < 0:
    print("Please enter a number: ")
elif instances > 0:
    print("Please wait")
    

print(" Results are processing ")


for str in range(1, instances + 1):
    EC2instance = thedepartment
    nameID = EC2instance + "-" + string_generator()
    print("The EC2 Instance Name : ", nameID)