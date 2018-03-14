# Add os and csv modules
import os
import csv

# Read csv file
file1 = "budget_data_1.csv"
with open(file1, newline="", encoding="latin-1" ) as bd1:
    data1 = csv.reader(bd1)

    # Save headers into header row
    header_row = next(data1)

    # Check the column index
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Create lists and variables
    dates = []
    revenue = []
    rev = 0
    rev1 = 0
    rev2 = 0
    revList = []
    revMax = 0
    revTotChg = 0

    # Loop through each row of data
    for row in data1:
        
        # Append each date to the list
        dates.append(row[0])

        # Convert data to integer and append each to list - sum
        rev = int(row[1])
        revenue.append(rev)

        # Calculate the difference
        rev2 = rev - rev1

        # Add the difference to the new list
        revList.append(int(rev2))
        # revTotChg.append()

        # Rewrite rev1 with current row value
        rev1 = rev
    
    # Find greatest increase; add to revMax
    revMax = max(revList)
    [i for i, j in enumerate(revList) if j == revMax]
    
    # Get index value of revMax
    revIn = revList.index(revMax)
    print(revIn)

    # Find greatest decrease; add to revMin
    revMin = min(revList)
    [i for i, j in enumerate(revList) if j == revMin]

    # Get index value of revMin
    revInd = revList.index(revMin)
    print(revInd)

    # Store values into variables for average change in revenue
    monTot = len(dates) 
    revTotChg = sum(revList)

    # Create a function to print all results
    def print_results():
        # print("Financial Analysis")
        # print("---------------------------------------")
        # print("Total Months: " + str(len(dates)))
        # print("Total Revenue: $" + str(sum(revenue)))
        # print("Average Change in Revenue: $"+ str(round(revTotChg/monTot, 2)))
        # print("Greatest Increase in Revenue: "+ str(dates[revIn]) + " ($" + str(revList[revIn])+ ")")
        # print("Greatest Decrease in Revenue: "+ str(dates[revInd]) + " ($" + str(revList[revInd])+ ")")

        # Create a variable inside the function
        result = "Financial Analysis\n"
        result = result + "File Name:" + file1 + "\n"
        result = result + "---------------------------------------\n"
        result = result + "Total Months: " + str(len(dates)) + "\n"
        result = result + "Total Revenue: $" + str(sum(revenue)) + "\n"
        result = result + "Average Change in Revenue: $"+ str(round(revTotChg/monTot, 2)) + "\n"
        result = result + "Greatest Increase in Revenue: "+ str(dates[revIn]) + " ($" + str(revList[revIn])+ ")\n" 
        result = result + "Greatest Decrease in Revenue: "+ str(dates[revInd]) + " ($" + str(revList[revInd])+ ")\n"
        return result 

    # Print results to terminal
    print(print_results())

    # Export results to a text file
    pyBank = open('pyBank.txt', 'w')
    print(pyBank)
    pyBank.write(print_results())

    # Export results - method 2 
    # pyBankHW = 'pyBankHW.txt'

    # with open(pyBankHW, 'w') as f:
    #     f.write(print_results()) 