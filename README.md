# Python_challenge #

## Objective ## 
The objective of the Python challenge is to create a Python script to run a csv file containing information regarding PyBank’s profit/losses for a period of 86 months.  The script should run and determine basic financial metrics and analysis for the data in the csv file.

## Approach ##
The script imports the csv file and reads it so it can create lists containing the Months and Profit/Loss for the month periods.  Next, the script counts the number of items in the Month list to determine the total number of periods and does an overall sum of the Profit Loss, after determining this data as integers, to determine the Net profit Loss for those periods.
To determine the average change in profit loss for the period, the script calculates the difference in the profit/loss amount between period and creates a sub list with the results.  The list with the change in profit/loss is then iterated to identify the Max and Minimum changes in profit.  Once those amounts have been determined, the script locates the index location on the changes list and iterates the list of months so it may present both the amount and the specific period when the Maximum and Minimum occurred in the period calculated.
Finally, the script prints the desired variables and creates and output file with the summary.

### Comments ###
As a person that is new to Python and coding in general, I utilized a simple approach by determining the data lists and variables needed to obtain the desired metrics by applying basic lists iterations and formulas.   The project was challenging but also a great opportunity to utilize basic python coding structures that helped me strengthen my understanding of the python coding logic.


## Resources:##

Berkeley's Fintech Bootcamp Activities repository for Python on Module 2.


For round number variable of the average change:
https://www.javatpoint.com/how-to-get-2-decimal-places-in-python#:~:text=To%20round%20the%20integer%20to,use%20the%20ceil()%20function
