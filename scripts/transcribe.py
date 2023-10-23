import os
import glob
import subprocess

# Set the paths for the input audio files and the output directory
input_dir = 'sw/eval'
output_dir = 'sw/tlogs'

# Get a list of all .wav files in the input directory
audio_files = glob.glob(os.path.join(input_dir, '*.wav'))

# Loop through each audio file
for audio_file in audio_files:
    # Set the output file path
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(audio_file))[0]+ '.tlog')
    
    # Run the Coqui STT inference command
    command = f"stt --model models/output_graph.tflite --audio {audio_file} > {output_file}"
    subprocess.run(command, shell=True)

    print(f"Inference completed for {audio_file}. Output saved to {output_file}")

print("All inference completed.")