#Alexis Ellis
#1/25/23

# websites used: https://realpython.com/python-string-contains-substring/
#                https://www.w3schools.com/python/python_file_open.asp
#                https://realpython.com/python-print/

x = "placeholder"

# will happen if the file is found
try:    

    # opens orginal file 
    newFile = open("snakeEx.txt", "r")

    # goes through all lines in file
    for line in newFile:
        #  assigns the line to a temp variable
        x = line
        # checks if work snake is the line and print if it is 
        if "snake" in x:
            print(line.rstrip())

        #  if snake is not in the line then it moves on and overides the x variable with the new 

    # closes orginal file
    newFile.close()


# will happen if file is not found
except:
    print("file not found try again.")
    
