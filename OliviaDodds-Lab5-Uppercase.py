#Olivia Dodds
#Python FA2026
#Due: November 19
#Lab 5: Uppercase
#Program reads a text file and converts all characters to uppercase, then writes the result to a new file.

def convertToUppercase():
    #open file to read
    with open("regular.txt", "r") as infile:
        #creates a string variable with the contents of the file
        contents = infile.read()

    #convert all characters to uppercase
    uppercase_contents = contents.upper()

    #write the uppercase contents to a new file
    with open("uppercase.txt", "w") as outfile:
        outfile.write(uppercase_contents)

convertToUppercase()
