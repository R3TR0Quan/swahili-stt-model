import json
import csv
import os

tlog_dir = "sw/eval"  # Path to the directory containing the .tlog files
csv_file = "sw/evaluation.csv"  # Path to the output CSV file

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["path", "sentence"])

    for tlog_file in os.listdir(tlog_dir):
        if tlog_file.endswith(".tlog"):
            tlog_path = os.path.join(tlog_dir, tlog_file)
            audio_path = os.path.splitext(tlog_path)
            with open(tlog_path, "r") as tlog:
                data = json.load(tlog)
                sentence = data["transcript"]
                writer.writerow([audio_path, sentence])