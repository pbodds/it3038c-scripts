import shutil
import time

# First part of this script will allow the user to choose between a 24hr clock or a 12hr clock format. After, the total space of your hard drive will be listed along 
# with the used space and free space.

loop = True
while loop == True:
    try:
        print("Welcome to the disk checker script! To be considerate, do you want your time formatted in (1) 12 hours or (2) 24 hours?")
        selectedTime = int(input())

        if selectedTime == 1:
            print(time.strftime("The time currently is: %I:%M:%S"))
            loop = False
            time.sleep(3) 

        elif selectedTime == 2:
            print(time.strftime("The time currently is: %H:%M:%S"))
            loop = False
            time.sleep(3)  
        
        else:
            print("Please enter (1) for 12 hour time format or (2) for 24 hour time format")
    except:
        print("Please enter a number")
        
total, used, free = shutil.disk_usage("/")

print("Time to check our hard drive space!")

print("Total: %d GB" % (total // (2**30)))
print("Used: %d GB" % (used // (2**30)))
print("Free: %d GB" % (free // (2**30)))



