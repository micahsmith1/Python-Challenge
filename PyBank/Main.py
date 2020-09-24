import os 
import csv 

budget_data = os.path.join("..", "PyBank", "Resources", "Budget_Data.csv")

total_mths = []
net_total = []

#Open budget_data
with open(budget_data, 'r')as fin_analysis:

    #Read budget_data
    csv_reader = csv.reader(fin_analysis, delimiter = ',')
    csv_header = next(csv_reader)

    for row in csv_reader:

        #Total Number of Months 
        total_mths.append(row[0])
        mths = len(total_mths)

        #Net Total Amount of "Profit/Losses"
        net_total.append(int(row[1]))
        total = sum(net_total)

    #Average of Changes in "Profits/Losses"
    average_change = []

    for i in range(len(net_total)-1):

        average_change.append(net_total[i+1]-net_total[i])

    #Calculate Average 
    avg = round(sum(average_change)/len(average_change),2)
    
    #Greatest Increase in Profits
    max_increase = max(average_change)
    #Correlate Greatest Increase with Month
    max_increase_mth = average_change.index(max(average_change)) + 1

    #Greatest Decrease in Losses 
    max_decrease = min(average_change)

    #Correlate Greatest Decrease with Month 
    max_decrease_mth = average_change.index(min(average_change)) + 1

    print(f'Financial Analysis')

    print(f'----------------------------')

    print(f'Total Months: {mths}')

    print(f'Total: ${total}')

    print(f'Average Change: ${avg}')

    print(f'Greatest Increase in Profits: {total_mths[max_increase_mth]} (${(str(max_increase))})')

    print(f'Greatest Increase in Profits: {total_mths[max_decrease_mth]} (${(str(max_decrease))})')


    #Output to Text File 
    file = open('output.txt', 'w')

    file.write('Financial Analysis' + '\n')

    file.write('----------------------------' + '\n')

    file.write(f'Total Months: {mths}' + '\n')

    file.write(f'Total: ${total}' + '\n')

    file.write(f'Average Change: ${avg}' +  '\n')

    file.write(f'Greatest Increase in Profits: {total_mths[max_increase_mth]} (${(str(max_increase))})' + '\n')

    file.write(f'Greatest Increase in Profits: {total_mths[max_decrease_mth]} (${(str(max_decrease))})')









    