import os
import glob
import subprocess
from multiprocessing import Pool
import yaml

#load env variables from yaml
with open('config.yaml', 'r') as conf:
    env_vars = yaml.safe_load(conf)

EVAL_DIR = env_vars['EVAL_DIR']
TLOGS_DIR = env_vars['TLOGS_DIR']

# Set the paths for the input audio files and the output directory
input_dir = EVAL_DIR
output_dir = TLOGS_DIR

# Get a list of all .wav files in the input directory
audio_files = glob.glob(os.path.join(input_dir, '*.wav'))

# Function to run the inference command for a single audio file
def run_inference(audio_file):
    # Set the output file path
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(audio_file))[0]+ '.tlog')
    
    # Run the Coqui STT inference command
    command = f"stt --model models/output_graph.tflite --audio {audio_file} > {output_file}"
    subprocess.run(command, shell=True)

    print(f"Inference completed for {audio_file}. Output saved to {output_file}")

# Create a pool of worker processes
pool = Pool(processes=6)

# Run the inference commands in parallel
pool.map(run_inference, audio_files)

# Close the pool of worker processes
pool.close()
pool.join()

print("All inference completed.")