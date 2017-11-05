import csv
with open('budget_data_1.csv', newline='') as csvfile:

        #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
    print("----------------!!")
    print(csvreader)
    print("----------------")
    print("Financial Analysis")
    print("------------------")
    #Print number of months aka rows
    data = list(csvreader)
    row_count = str(len(data)-1)
    print("Total Months: " + row_count)
    
    #The total amount of revenue gained over the entire period
with open('budget_data_1.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    revenue = []
    next(csvreader)

  #puts values of rev column into list  
    for row in csvreader:
       revenue.append(int(row[1]))
converted_revenue = sum(revenue)
print('_____')
converted_revenue = str(converted_revenue)
print("Total Revenue: " + converted_revenue)

#Average revenue change

ind = 0
for row in revenue:
        ind = int(ind) + 1
        changes = revenue[ind] - revenue[ind +1]
        changes_sum = 0
        changes_sum += (changes)
        if ind >38:
            break
avg_rev_row = (changes)/40
print('_______-')
print(changes_sum)   
print(avg_rev_row) 
    
    
    
    
#     ind = revenue.index(row)
 #sum_rev_row = (int(revenue[0])-int(rev_row[1])) + (int(rev_row[1])-int(rev_row[2])) + (int(rev_row[2])-int(rev_row[3])) + (int(rev_row[3])-int(rev_row[4])) + (int(rev_row[4])-int(rev_row[5])) + (int(rev_row[5])-int(rev_row[6])) + (int(rev_row[6])-int(rev_row[7])) + (int(rev_row[7])-int(rev_row[8]))+ (int(rev_row[8])-int(rev_row[9]))+ (int(rev_row[9])-int(rev_row[10]))+ (int(rev_row[10])-int(rev_row[11]))+ (int(rev_row[11])-int(rev_row[12]))+ (int(rev_row[12])-int(rev_row[13]))+ (int(rev_row[13])-int(rev_row[14]))+ (int(rev_row[14])-int(rev_row[15]))+ (int(rev_row[15])-int(rev_row[16]))+ (int(rev_row[16])-int(rev_row[17]))+ (int(rev_row[17])-int(rev_row[18]))+ (int(rev_row[18])-int(rev_row[19]))+ (int(rev_row[19])-int(rev_row[20]))+ (int(rev_row[20])-int(rev_row[21]))+ (int(rev_row[21])-int(rev_row[22]))+ (int(rev_row[22])-int(rev_row[23]))+ (int(rev_row[23])-int(rev_row[24]))+ (int(rev_row[24])-int(rev_row[25]))+ (int(rev_row[25])-int(rev_row[26]))+ (int(rev_row[26])-int(rev_row[27]))+ (int(rev_row[27])-int(rev_row[28]))+ (int(rev_row[28])-int(rev_row[29]))+ (int(rev_row[29])-int(rev_row[30]))+ (int(rev_row[30])-int(rev_row[31]))+ (int(rev_row[31])-int(rev_row[32]))+ (int(rev_row[32])-int(rev_row[33]))+ (int(rev_row[33])-int(rev_row[34]))+ (int(rev_row[34])-int(rev_row[35]))+ (int(rev_row[35])-int(rev_row[36]))+ (int(rev_row[36])-int(rev_row[37])) + (int(rev_row[37])-int(rev_row[38]))+ (int(rev_row[38])-int(rev_row[39])) + (int(rev_row[39])-int(rev_row[40]))
# avg_rev_row = sum_rev_row/40
# print('Avg Rev Change: ' + " " + "$" + str(avg_rev_row))
# print('_______')





    
    
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period


#candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Sweedish Fish", "Skittles", "Hershey Bar", "Skor", "Starburst", "M&Ms"]
#print(candy_list)
#candy_cart = []
#allowance = 3
#for candy_name in candy_list:
#    ind = candy_list.index(candy_name)
#    print (str(ind) + " " + candy_name)

#Run through a loop which allows the user to choose wihch candy to take home with them
#for x in range(allowance):
#    selected = input("which candy would you like to bring home? ")

#add the candy at the index chosen to the candy_cart list
#    candy_cart.append(candy_list[int(selected)])

#print("I brought home with me..." )
#for candy_name in candy_cart:
#    print(candy_name)

#candy_list.append(8)
#Allowance = 3
#print(candy_list[1])
#list.index(8)

#for candy_list in range(9):
#    print(candy_list)