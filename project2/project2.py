import shutil
import time
import platform
from fpdf import FPDF

#IMPORTANT! FPDF NEEDS TO BE INSTALLED. "pip install fpdf"

# First part of this script will allow the user to choose between a 24hr clock or a 12hr clock format. After, the total space of your hard drive will be listed along 
# with the used space and free space. Following that will be a basic script that takes system information and stores it into a .txt file and converts it to a PDF. 

loop = True
while loop == True:
    try:
        print("Welcome to the disk checker script! To be considerate, do you want your time formatted in (1) 12 hours or (2) 24 hours?")
        selectedTime = int(input())

        if selectedTime == 1:
            print(time.strftime("The time currently is: %I:%M:%S %p"))
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


# getting variables in the order of the tuple (total, used, free). "/" defines the path for the drive (drive used depends on directory of file)
total, used, free = shutil.disk_usage("/")

# dividing variables by 1024**3 as given variables are returned in bytes and want to covert to GB, with 1024 bytes in a KB * 1024 for Megabyte * 1024 for Gigabyte
print("Time to check our hard drive space!")
print("Total: %d GB" % (total // (1024**3)))
print("Used: %d GB" % (used // (1024**3)))
print("Free: %d GB" % (free // (1024**3)))

# Setting printed file to 0 as the file has not been printed yet. Running it through a while loop to create the file, print it to a pdf, and exit. 
printedFile = 0

while printedFile == 0:
# Creating a file named sysinfo in a write state. The file will be created in whatever file path the terminal is currently in.
    file = open('sysInfo.txt', 'w')
#writing to the file
    file.write("Let's learn more about your system! \n")
    file.write("Your platform processor is: " + str(platform.processor()) + "\n")
    file.write("Your system's name is: " + str(platform.node()) + "\n")
    file.write("Your system is: " + str(platform.system()) + "\n")
    file.write("Finally, your processor is: " + str(platform.platform()) + "\n")
    file.write("If you forgot how much storage is on your hard drive: \n")
    file.write("Total: %d GB " % (total // (1024**3)))
    file.write("Used: %d GB " % (used // (1024**3)))
    file.write("Free: %d GB " % (free // (1024**3)))
    file.close()

# Creation for .txt to .pdf format. Creating a pdf variable set to FPDF module and creating a page
    pdf = FPDF()
    pdf.add_page()
# Setting the font type, making the text bold, and setting the font size to 15
    pdf.set_font("Times", 'B', size = 15)
#fToP is file to PDF, opening our previously created .txt file and reading it
    fToP = open('sysInfo.txt', 'r')
#For each line in fToP, a result will be printed. Creating a cell for the information to go into. No border is set, so you will not see the cell outline.
# In order, setting the: width, height, the text to be written, ln is setting the position to the beginning of the line, and aligning the document to the left.
    for line in fToP:
        pdf.cell(200, 10, txt = line, ln = 1, align = 'L')
# Outputting the final document to a PDF   
    pdf.output("sysInfo.pdf")
#Ending the while loop
    printedFile = 1