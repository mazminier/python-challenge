# Add os and csv modules
import os
import csv

# Read csv file
file1 = "election_data_1.csv"
with open(file1, newline="", encoding="latin-1" ) as bd1:
    data1 = csv.reader(bd1)

    # Save headers into header row
    header_row = next(data1)

    # Check the column index
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Create lists and variables
    tot_votes = 0
    voters_all = []
    county_all = []
    candidates_all = []
    candidates = []
    candidate_n = ""

    # Loop through each row of data
    for row in data1:
        
        # Add each column into a list
        voters_all.append(row[0])
        county_all.append(row[1])
        candidates_all.append(row[2])

        # Tally number of votes
        tot_votes = tot_votes + 1

        candidate1 = row[2]
    print(tot_votes)

    #     current = True
    #     while current:
            
    #         if candidate1 not in candidates:
    #             candidates.append(candidate1)


                

    print(len(candidates_all))

    print(tot_votes)


        
                
        

            
# print(candidates)
# use while loop to count 


    # Create a function to print all results
    def print_results():
    

    #     # Create a variable inside the function
    #     result = "Election Results\n"
    #     result = result + "---------------------------------------\n"
    #     result = result + "Total Votes:" + tot_votes + "\n"
    #     result = result + "---------------------------------------\n"
    #     result = result + "Candidate 1: " + str(len(dates)) + "\n"
    #     result = result + "Candidate 2:" + str(sum(revenue)) + "\n"
    #     result = result + "Candidate 3: $"+ str(round(revTotChg/monTot, 2)) + "\n"
    #     result = result + "Candidate 4: "+ str(dates[revIn]) + " ($" + str(revList[revIn])+ ")\n" \
    #     result = result + "---------------------------------------\n"
    #     result = result + "Winner: "+ str(dates[revInd]) + " ($" + str(revList[revInd])+ ")\n"
    #     result = result + "---------------------------------------\n"
    #     return result 

    # # Print results to terminal
    # print(print_results())

    # # Export results to a text file
    # pyPoll = open('pyPoll.txt', 'w')
    # print(pyPoll)
    # pyPoll.write(print_results())