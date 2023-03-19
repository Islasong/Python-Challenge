#import Modules
import os
import csv


#Define the variables
months = []
profit_loss_changes = []

#set the initial data
month_count = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

#set path for file
csvpath = os.path.join("Resources", "budget_data.csv")



#open and Reading using CSV module
with open(csvpath) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # reading header row
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    #Read each row of data
    for row in csvreader: 
        month_count = month_count + 1

        #The net total amount of profit/loss over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss = net_profit_loss + current_month_profit_loss

        if month_count == 1:
            previous_month_profit_loss = current_month_profit_loss
            
        
        else:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            
            months.append(row[0])
            
            profit_loss_changes.append(profit_loss_change)
            previous_month_profit_loss = current_month_profit_loss


        
# the total changes of profit and loss and the average change
total_changes = sum(profit_loss_changes)
average_change = round(total_changes/(month_count-1),2)

# the greatest increase and decrease
greatest_increase = max(profit_loss_changes)
greatest_increase_month = profit_loss_changes.index(greatest_increase)
Best_month = months[greatest_increase_month]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_month = profit_loss_changes.index(greatest_decrease)
worst_month = months[greatest_decrease_month]

#print
print("Financial Aalysis")
print("-------------------------------------")
print(f"Total Months:  {month_count}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits:  {Best_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits:  {worst_month} (${greatest_decrease})")

#Export a text file
#Specify the file to write to
budget_result_file = os.path.join("Output", "result_data.txt")

#Open the file using "write" mode.
with open(budget_result_file, "w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("------------------------------\n")
    datafile.write(f"Total Months:  {month_count}\n")
    datafile.write(f"Total:  ${net_profit_loss}\n")
    datafile.write(f"Average Change:  ${average_change}\n")
    datafile.write(f"Greatest Increase in Profits:  {Best_month} (${greatest_increase})\n")
    datafile.write(f"Greatest Decrease in Profits:  {worst_month} (${greatest_decrease})\n")




      


















