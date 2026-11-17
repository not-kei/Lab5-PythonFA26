#Olivia Dodds
#Python FA2026
#Due: November 19
#Lab 4: TempConvert
#Program converts temperatures from Fahrenheit to Celsius and writes the results to a text file.

def writeTempTable():

    #open the file to write
    with open("tempConv.txt", "w") as file:

        #write the column headings
        file.write(f"{'Fahrenheit':>10}{'Celsius':>10}\n")

        #convert temperatures from -300 to 212
        for fahrenheit in range(-300, 213):
            celsius = (fahrenheit - 32) * 5 / 9

            #write temperatures with 3 decimal places
            file.write(f"{fahrenheit:10.3f}{celsius:10.3f}\n")

writeTempTable()