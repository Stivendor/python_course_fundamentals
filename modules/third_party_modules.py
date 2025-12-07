# third party modules are modules that are not included in the standard library but can be installed via package managers like pip
# in this case, we will use the pandas module to read a csv file

import pandas # import pandas module to work with dataframes
import os # os module provides functions to interact with the operating system
import time # time module to add delay

print("Checking for the existence of vegetables.txt every 5 seconds:")
while True:
    if os.path.exists("../files/temps_today.csv"):
        data = pandas.read_csv("../files/temps_today.csv") # read the csv file using pandas
        print(data.mean()) # print the mean of each column
    else:
        print("File not found. Please check the path.")
    time.sleep(5)  # wait for 10 seconds before checking again