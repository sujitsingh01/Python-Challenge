import os,csv

total_months = 0
total_profit = 0
total_change = 0
greatest_month =''
lowest_month =''
max_change = 0
max_index = 0
min_change = 0
min_index = 0
i = 0
difference = 0
max_month = ' '
min_month = ' '
total = []
month =[]

output_path = os.path.join('budget_data_analysed.csv')
file_path = os.path.join('budget_data.csv')

with open (file_path, 'r',newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_months += 1
        total_profit += int(row[1])
        total.append(row[1])
        month.append(row[0])
        
    #print(month)
    
    for i in range(0,len(total)-1):
        if (total[i] != total[i+1]): 
            new_change =  int(total[i+1]) - int(total[i])
            difference = difference + new_change
            if ( new_change > max_change):
                max_change = new_change
                max_index = i+1
            if ( new_change < min_change):
                min_change = new_change
                min_index = i+1
            
    avg_difference = round( difference / ( total_months -1 ) ,2)
       
    for i in range(0,len(month)): 
        
        if ( i == int(max_index)): 
            max_month = month[i]
        
        if ( i == int(min_index)):
            min_month = month[i]
print('Financial Analysis')
print('--------------------------------')
print(f'Total Months : {total_months}')
print(f'Total : ${total_profit}')
print(f'Average Change : ${avg_difference}')
print(f'Greatest Increase in Profits: {max_month} $({max_change})')
print(f'Greatest Decrease in Profits: {min_month} $({min_change})')


with open(output_path,'w') as output_file:
    print(f'Financial Analysis', file=output_file)
    print('--------------------------------',file=output_file)
    print(f'Total Months : {total_months}', file=output_file)
    print(f'Total : ${total_profit}',file=output_file)
    print(f'Average Change : ${avg_difference}',file=output_file)
    print(f'Greatest Increase in Profits: {max_month} $({max_change})',file=output_file)
    print(f'Greatest Decrease in Profits: {min_month} $({min_change})',file=output_file)

