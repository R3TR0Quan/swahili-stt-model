import csv
import os

tlog_dir = "sw/tlogs"  # Path to the directory containing the .tlog files
csv_file = "sw/submission.csv"  # Path to the output CSV file

data = []

for filename in os.listdir(tlog_dir):
    if filename.endswith('.tlog'):
        file_path = os.path.join(tlog_dir, filename)
        
        # Open the .tlog file and read the sentence
        with open(file_path, 'r') as file:
            sentence = file.read().strip()
        
        # Create the row for the CSV file
        row = [filename.replace('.tlog', '.mp3'), sentence]
        
        # Append the row to the data list
        data.append(row)
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['path', 'sentence'])  # Write the header row
    writer.writerows(data)  # Write the data rows