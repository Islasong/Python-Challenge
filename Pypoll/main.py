import os
import csv


#define the variable
votes_cast = []
candidates = []

pypoll_csvpath = os.path.join("Resources","election_data.csv")

#open and read csvfile
with open (pypoll_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #read header
    csv_header = next(csvreader)
    #print header
    #print(f"Header: {csv_header}")

    for column in csvreader:
        votes_cast.append(column[0])
        candidates.append(column[2])
    
    #counts of the total votes
    total_votes = len(votes_cast)
    #print(f"total votes:  {total_votes}")

    #counts of each candidate votes
    Charles_C_S = int(candidates.count("Charles Casper Stockham"))
    Diana_D = int(candidates.count("Diana DeGette"))
    Raymon_A_D = int(candidates.count("Raymon Anthony Doane"))

    #votes percentage for each candidate
    Charles_percentage = (Charles_C_S/total_votes)*100
    Diana_percentage = (Diana_D/total_votes)*100
    Raymon_percentage = (Raymon_A_D/total_votes)*100

    Adjusted_Charles_percentage = round(Charles_percentage,3)
    Adjusted_Diana_percentage = round(Diana_percentage,3)
    Adjusted_Raymon_percentage = round(Raymon_percentage,3)


    if Charles_C_S > Diana_D > Raymon_A_D:
        Winner = "Charles Casper Stockham"

    elif Diana_D > Charles_C_S > Raymon_A_D:
        Winner = "Diana DeGette"

    else:
        Winner = "Raymon Anthony Doane"

    #print result
    print("Election Results")
    print("--------------------------------")
    print(f"Total Votes:  {total_votes}")
    print("--------------------------------")
    print(f"Charles Casper Stockham:  {Adjusted_Charles_percentage}% ({Charles_C_S})")
    print(f"Diana Degette:  {Adjusted_Diana_percentage}% ({Diana_D})")
    print(f"Raymon Anthony Doane:  {Adjusted_Raymon_percentage}% ({Raymon_A_D})")
    print('---------------------------------')
    print(f"Winner:  {Winner}")


#Export result
file = os.path.join("analysis", "election_result.txt")
with open(file, "w") as datafile:
    datafile.write("Election Results\n")
    datafile.write("------------------------\n")
    datafile.write(f"Total Votes:  {total_votes}\n")
    datafile.write("------------------------\n")
    datafile.write(f"Charles Casper Stockham:  {Adjusted_Charles_percentage}% ({Charles_C_S})\n")
    datafile.write(f"Diana Degette:  {Adjusted_Diana_percentage}% ({Diana_D})\n")
    datafile.write(f"Raymon Anthony Doane:  {Adjusted_Raymon_percentage}% ({Raymon_A_D})\n")
    datafile.write("------------------------\n")
    datafile.write(f"Winner:  {Winner}\n")















