import os
import csv

# set empty lists
months = []
revenue = []
average_change = []

# define variables
prev_month = 0
total_months = 0
total_revenue = 0
total_rev_change = 0
highest_increase = 0
biggest_loss = 999999999

# create file path
csvpath = os.path.join('..','PyBank','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    first_row = next(csvreader)
    #print(f"CVS Header: {csv_header}")
    months.append(first_row[0])
    revenue.append(int(first_row[1]))
    prev_month = int(first_row[1])

    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
        net_change = int(row[1])-prev_month
        
        average_change.append(int(row[1])-prev_month)
        prev_month = int(row[1])
        if net_change > highest_increase:
            highest_increase = net_change
            highest_increase_month = row[0]
        if net_change < biggest_loss:
            biggest_loss = net_change
            biggest_loss_month = row[0]

# more variables defined
total_months = len(months)
total_revenue = sum(revenue)
average_change_all = sum(average_change)/len(average_change)

# show calculations
#print(total_months)
#print(total_revenue)
#print(average_change_all)
#print(highest_increase)
#print(highest_increase_month)
#print(biggest_loss)
#print(biggest_loss_month)

# sets and opens the output destination in write mode and prints the summary
file = '../PyBank/input.txt'
with open(file,'w') as writefile:
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change_all) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + highest_increase_month + ' ($' + str(highest_increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + biggest_loss_month + ' ($' + str(biggest_loss) + ')')

# opens the output file in r mode and prints to terminal
with open(file, 'r') as readfile:
    print(readfile.read())


#The total number of months included in the dataset
## count how many rows are in the date column

#The total net amount of "Profit/Losses" over the entire period
## sum up all rows under profit/loss

#The average change in "Profit/Losses" between months over the entire period
## B3-B2=116,771 ; B4-B3=-662,642 and so on..at the end average all these together

#The greatest increase in profits (date and amount) over the entire period
## this is between jan and feb 2012

#The greatest decrease in losses (date and amount) over the entire period
## this is between Aug and Sep 2013

#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

