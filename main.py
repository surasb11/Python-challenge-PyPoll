import csv
import os

inputFileName = "budget_data.csv"
outputFileName = os.path.splitext(inputFileName)[0] + "_analyze.csv"

with open(inputFileName, newline='') as inFile, open(outputFileName, 'w', newline='') as outfile:
  r = csv.reader(inFile)
  w = csv.writer(outfile)

  next(r, None)
    
  w.writerow(['Date', 'Profit_Losses'])

  for row in r:
    w.writerow(row)
    
budget_csv_path = os.path.join("budget_data_analyze.csv")

with open(budget_csv_path, newline="") as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=",")
  
  csv_header = next(csv_reader)
  print(f"CSV Header: {csv_header}")


inputFileName = "budget_data_analyze.csv"
outputFileName = "budget_data_analyze.txt"

total_months = 0
total_profit = 0


prev_profit = 0
profit_change = 0

greatest_increase_profits = ["", 0]
greatest_decrease_profits = ["", 9999999999999999999999]

profit_changes = []


with open(inputFileName) as profit_data:
  reader = csv.DictReader(profit_data)
  
  
  for row in reader:
    
    total_months = total_months + 1
    total_profit = total_profit + int(row["Profit_Losses"])

    
    profit_change = int(row["Profit_Losses"]) - prev_profit
    
    prev_profit = int(row["Profit_Losses"])
    
    if (profit_change > greatest_increase_profits[1]):
      greatest_increase_profits[1] = profit_change
      greatest_increase_profits[0] = row["Date"]

    if (profit_change < greatest_decrease_profits[1]):
      greatest_decrease_profits[1] = profit_change
      greatest_decrease_profits[0] = row["Date"]
      
    profit_changes.append(int(row["Profit_Losses"]))    

    
  profit_avg = sum(profit_changes) / len(profit_changes)
  

  print()
  print()
  print()
  
  print("Financial Analysis")
  
  print("-------------------------")
  
  print("Total Months: " + str(total_months))
  print("Total: " + "$" + str(total_profit))
  print("Average Change: " + "$" + str(round(sum(profit_changes) / len(profit_changes),2)))
  print("Greatest Increase in Profits: " + str(greatest_increase_profits[0]) + " ($" +  str(greatest_increase_profits[1]) + ")") 
  print("Greatest Decrease in Profits: " + str(greatest_decrease_profits[0]) + " ($" +  str(greatest_decrease_profits[1]) + ")")


with open(outputFileName, "w") as txt_file:
  txt_file.write("Total Months: " + str(total_months))
  txt_file.write("\n")
  txt_file.write("Total: " + "$" + str(total_profit))
  txt_file.write("\n")
  txt_file.write("Average Change: " + "$" + str(round(sum(profit_changes) / len(profit_changes),2)))
  txt_file.write("\n")
  txt_file.write("Greatest Increase in Profits: " + str(greatest_increase_profits[0]) + " ($" + str(greatest_increase_profits[1]) + ")") 
  txt_file.write("\n")
  txt_file.write("Greatest Decrease in Profits: " + str(greatest_decrease_profits[0]) + " ($" + str(greatest_decrease_profits[1]) + ")")