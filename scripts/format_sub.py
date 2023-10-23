import csv
import os
import yaml

#load env variables from yaml
with open('config.yaml', 'r') as conf:
    env_vars = yaml.safe_load(conf)

TLOGS_DIR = env_vars['TLOGS_DIR']# Path to the directory containing the .tlog files
SUBMISSION_CSV = env_vars['SUBMISSION_CSV']# Path to the output CSV file

data = []

for filename in os.listdir(TLOGS_DIR):
    if filename.endswith('.tlog'):
        file_path = os.path.join(TLOGS_DIR, filename)
        
        # Open the .tlog file and read the sentence
        with open(file_path, 'r') as file:
            sentence = file.read().strip()
        
        # Create the row for the CSV file
        row = [filename.replace('.tlog', '.mp3'), sentence]
        
        # Append the row to the data list
        data.append(row)
with open(SUBMISSION_CSV, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['path', 'sentence'])  # Write the header row
    writer.writerows(data)  # Write the data rows