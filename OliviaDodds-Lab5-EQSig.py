#Olivia Dodds
#Python FA2026
#Due: November 19
#Lab 4: EQSig
#Program retrieves earthquake data from the USGS website and calculates statistics on the significance values 
#of earthquakes in the past month.

#importing necessary libraries
import json
import urllib.request
import statistics 

#Retrieving earthquake data from the USGS website
handle = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson")

#Reading the data from the URL and loading it as a JSON object
data = handle.read()
eData = json.loads(data)

#Extracting the list of earthquakes from the JSON object
earthquakeList = eData["features"]

sigList = []

#Calculating statistics on the significance values of earthquakes
for earthquake in earthquakeList:
    sig = earthquake.get("properties").get("sig")
    sigList.append(sig)

#Calculating the min and max significant values
minimum = min(sigList)
maximum = max(sigList)

#Calculating the mean, median, standard deviation, and mode of the significant values
mean = statistics.mean(sigList)
median = statistics.median(sigList)
stdev = statistics.stdev(sigList)
modes = statistics.mode(sigList)

#Printing the calculated statistics
print("The minimum sig is", format(minimum, ".3f"))
print("The maximum sig is", format(maximum, ".3f"))
print("The mean sig is", format(mean, ".3f"))
print("The median sig is", format(median, ".3f"))
print("The standard deviation of sig is", format(stdev, ".3f"))
print("The mode(s) of sig are:", format(modes, ".3f"))