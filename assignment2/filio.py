# Implement a program that reads a CSV file named "data.csv," containing columns
# "Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
# individuals who are 18 years or older.
"""
This module contains examples of file input and output in Python.
"""

import os
import csv
import json

def filter_adults(input_file, output_file):
    """
    Read a CSV file containing "Name" and "Age" columns,
    filter adults (age >= 18), and save to a new CSV file.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_file)
    output_file = os.path.join(script_dir, output_file)

    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        read = csv.DictReader(csvfile)
        adults = [row for row in read if int(row['Age']) >= 18]

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(adults)

INPUT_FILE = "data.csv"
OUTPUT_FILE = "adults.csv"

filter_adults(INPUT_FILE, OUTPUT_FILE)

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

def add_to_json(input_file, new_data):
    """
    Read a JSON file, add new data, and write back to the same file.
    """
    try:
        # Get the absolute path of the file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, input_file)

        # Read existing JSON data from the file
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Append the new_data dictionary to the list
        data.append(new_data)

        # Write the updated data back to the file
        with open(input_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

        print("Data added successfully!")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{input_file}' does not contain valid JSON data.")

# Sample JSON data
INPUT_FILE = "data.json"
NEW_DATA = {
    "name": "Laxman",
    "age": 28
}

add_to_json(INPUT_FILE, NEW_DATA)

# Create a function search_log that takes a log file and a search keyword as input.
# The function should find and display all lines containing the search keyword.

def search_log(log_file, search_keyword):
    """
    Search and display lines containing the search keyword in a log file.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        log_file = os.path.join(script_dir, log_file)

        with open(log_file, 'r', encoding='utf-8') as file:
            for line in file:
                if search_keyword in line:
                    print(line.strip())  # Remove newline from the line

    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")

# Sample usage
LOG_FILE = "logfile.txt"
SEARCH_KEYWORD = "ERROR"

search_log(LOG_FILE, SEARCH_KEYWORD)
