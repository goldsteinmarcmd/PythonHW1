import csv
with open('budget_data_1.csv', newline='') as csvfile:

        #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
    print("Financial Analysis")
    print("------------------")
    #Print number of months aka rows
    data = list(csvreader)
    row_count = str(len(data))
    print("Total Months: " + row_count)
    
    #The total amount of revenue gained over the entire period
  

#with open('budget_data_1.csv', newline='') as csvfile:
 #   total = 0
  #  for row in csv.reader(csvfile):
   #     total += int(row[1])
   # print(total)

#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period