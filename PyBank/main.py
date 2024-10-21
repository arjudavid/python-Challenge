# Importing files
import csv
import os

# Files to load and output 
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
greatest_increase = {"date": 0, "value": float('-inf')}
greatest_decrease = {"date": 0, "value": float('inf')}
netchange = 0
netchange_list= []
previous_value = None
dates = []
date = None

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        # Track the total
        date = row[0]
        current_value = int(row[1])

        # Track the net change
        total_net += current_value

        if previous_value != None:
            netchange = current_value - previous_value
            netchange_list.append(netchange) 

        previous_value = current_value

        # Calculate the greatest increase in profits (month and amount)
        if netchange > greatest_increase["value"]:
                greatest_increase["value"] = netchange
                greatest_increase["date"] = date

        # Calculate the greatest decrease in losses (month and amount)
        if netchange < greatest_decrease["value"]:
                greatest_decrease["value"] = netchange
                greatest_decrease["date"] = date

        dates.append(date)

# Calculate the average net change across the months
average = sum(netchange_list) / len (netchange_list)

total_months = len (dates)


# Generate the output summary
summary_table = (
        f"Finnancial Analysis\n"
        f"-------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net:,.0f}\n"
        f"Average Change: ${average:,.0f}\n"
        f"Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["value"]:,.0f})\n"
        f"Greatest Decrease in Profits: {greatest_increase["date"]} (${greatest_decrease["value"]:,.0f})\n")


# Print the output
print (summary_table)


# Write the results to a text file

with open(file_to_output, "w") as txt_file:
  txt_file.write(summary_table)
