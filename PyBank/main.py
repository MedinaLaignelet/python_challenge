#!/usr/bin/env python
# coding: utf-8




#import the pathlib and csv library
from pathlib import Path
import csv





# Set File path
csvpath = Path('budget_data.csv')





#Initialize number variable
#initialize Variable to hold Profit/Loss and Months
line_num = 0
Profitloss = []
Months = []
change= []





# Open the input path as a file object
# Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    
with open(csvpath,"r") as csvfile:
    
    print(type(csvfile))
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next (csvreader)
    line_num +=1
    
    print(f"{header}<---HEADER")
    
    #Create lists Months and profitloss for values on Rows in cvs file:
    for row in csvreader:
        print(row)
        Date = row[0]
        Months.append(Date)
        Profitlosses = int (row[1])
        Profitloss.append(Profitlosses)





Months





Profitloss


# In[7]:


#Check Type of item for months list
type (Months)





#Check TProfitlossesype of item for months list
type (Profitlosses)





# Initialize the metric variables
count = 0
total = 0
change= 0
changesum= 0
average = 0
changeaverage= 0
greatest_increase = 0
greatest_month = 0
greatest_decrease = 0




len (Months)




#To count the number of months on the CSV file:
count = len (Months)





#To Calculate cummulative sum total :
for Profitlosses in Profitloss:
    #sum total and count variables
    total += Profitlosses
    count += 1
    





Profitloss





#Create list with revenue chnage per monht

change = [Profitloss[i+1]-Profitloss[i] for i in range(len (Profitloss) -1)]




change





count= len (Months)




count





#sum total and count variables
changesum= sum(change)




changesum





# Calculate average of chnagesum 
changeaverage = (changesum / (count -1))
 




changeaverage





# rounding the above number   
rounded_number = format(changeaverage, ".2f")





rounded_number





# to find the Minimum (Greates Decrease) in the average change





greatest_decrease = min (change)





greatest_decrease





# to find the Maximum (Greatest Increase) in the average change
greatest_increase = max (change)





greatest_increase





#Create Variable for Max and Min index location:
index_min_loc: []
index_max_loc: []





#locate index for Min in Profit /Loss in change:
index_min_loc = (change.index(greatest_decrease))





index_min_loc





#locate index for MaX in Profit /Loss change:
index_max_loc = (change.index(greatest_increase))





index_max_loc





#create variable for Min in Profit month position:
indexmin=0
indexmax =0





indexmin = (index_min_loc + 1)





indexmin





indexmax = (index_max_loc + 1)





indexmax





monthmin = print (Months[indexmin])





monthmax = print (Months[indexmax])





# Print out the summary statistics
print("---------Financial Analysis----------")
print("-------------------------------------")
print (f"Number of Months: {count}")
print(f"Total Profits/Losses:${total}")
print(f"Average: ${rounded_number}")
print(f"Worst Loss: ${greatest_decrease} {Months[indexmin]}")
print(f"Best Gain: ${greatest_increase} {Months[indexmax]}")





#set Output header and results
header = ["---------------------------Financial Analysis--------------------------------"]
space = ["------------------------------------------------------------------------------"]
metricA =  (f"Number of Months: {count}")
metricB = (f"Total Profits/Losses: {total}")
metricC = (f"Average: {rounded_number}")
metricD = (f"Worst Loss: ${greatest_decrease}{Months[indexmin]}")
metricE = (f"Best Gain: ${greatest_increase}{Months[indexmax]}")         





#Set up output in file
output_path = Path ('output.csv')





with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow (header)
    csvwriter.writerow (space)
    csvwriter.writerow(metricA)
    csvwriter.writerow(metricB)
    csvwriter.writerow(metricC)
    csvwriter.writerow(metricD)
    csvwriter.writerow(metricE)






























