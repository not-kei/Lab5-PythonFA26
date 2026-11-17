#Olivia Dodds
#Python FA2026
#Due: November 19
#Lab 4: Uppercase

def convertToUppercase():
    #open file to read
    with open("regular.txt", "r") as infile:
        contents = infile.read()

    #convert all characters to uppercase
    uppercase_contents = contents.upper()

    #write the uppercase contents to a new file
    with open("uppercase.txt", "w") as outfile:
        outfile.write(uppercase_contents)

convertToUppercase()