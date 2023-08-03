# Implement a program that reads a CSV file named "data.csv," containing columns
# "Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
# individuals who are 18 years or older.
import os
import csv

def filter_adults(input_file, output_file):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_file)
    output_file = os.path.join(script_dir, output_file)
    with open(input_file, 'r', newline='') as csvfile:
        read = csv.DictReader(csvfile)
        print(read)
        adults = [row for row in read if int(row['Age']) >= 18]

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(adults)

input_file = "data.csv"
output_file = "adults.csv"

filter_adults(input_file, output_file)

# Create a function add_to_json that takes a filename and a dictionary as input. The
# function should read the JSON data from the file, add the new dictionary to it, and
# write the updated data back to the same file.
# ○ Sample Json:
# [
# {
# "name": "Ram",
# "age": 30
# },
# {
# "name": "Sita",
# "age": 25
# }
# ]

import json
import os

def add_to_json(input_file, new_data):
    try:
        # Get the absolute path of the file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, input_file)

        # Read existing JSON data from the file
        with open(input_file, 'r') as file:
            data = json.load(file)

        # Append the new_data dictionary to the list
        data.append(new_data)

        # Write the updated data back to the file
        with open(input_file, 'w') as file:
            json.dump(data, file, indent=2)

        print("Data added successfully!")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{input_file}' does not contain valid JSON data.")

# Sample JSON data
input_file = "data.json"
new_data = {
    "name": "Laxman",
    "age": 28
}

add_to_json(input_file, new_data)

# Create a function search_log that takes a log file and a search keyword as input.
# The function should find and display all lines containing the search keyword.

def search_log(log_file, search_keyword):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        log_file = os.path.join(script_dir, log_file)
        with open(log_file, 'r') as file:
            for line in file:
                if search_keyword in line:
                    print(line.strip())  # Remove newline from the line

    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")

# Sample usage
log_file = "logfile.txt"
search_keyword = "ERROR"

search_log(log_file, search_keyword)
