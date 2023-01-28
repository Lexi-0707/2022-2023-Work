#1/25/23

# wesbites used: https://www.quora.com/How-do-I-add-new-line-in-the-first-line-in-a-text-file-using-Python
#                https://pynative.com/python-write-list-to-file/

list = []
firstLine = True 

# will happen if the file is there
try:    

    # opens orginal file 
    openFile = open("reverseEx.txt")

    # adds each line to a list 
    for line in openFile:
        list.append(line)

    # closes orginal file
    openFile.close()

    # creates new file
    newFile = open("newFile.txt", "w")
    #  goes through the list variable reversed and writes each line
    for item in reversed(list):
        #  checks if it is the first line. If it is then it adds a new line 
        if firstLine == True:
            newFile.write(item + "\n")
            firstLine = False
        # other it writes the line to the file
        else:
            newFile.write(item)

    # closes file I am writing in
    newFile.close()

    # opens file to read 
    newFile = open("newFile.txt", "r")

    # reads file
    newFile.read()

    # closes new file
    newFile.close()

# will happen if file is not in folder
except:
    print("file not found try again")
    
