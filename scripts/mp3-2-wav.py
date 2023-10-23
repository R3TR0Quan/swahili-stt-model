import os
import sys
from pydub import AudioSegment

def convert_mp3_to_wav(directory):
    # Get a list of all files in the directory
    file_list = os.listdir(directory)

    # Filter out non-MP3 files
    mp3_files = [file for file in file_list if file.lower().endswith('.mp3')]

    # Convert each MP3 file to WAV
    for mp3_file in mp3_files:
        mp3_path = os.path.join(directory, mp3_file)
        wav_file = mp3_file[:-4] + '.wav'
        wav_path = os.path.join(directory, wav_file)

        # Load MP3 file
        audio = AudioSegment.from_mp3(mp3_path)

        # Resample to 16kHz
        audio = audio.set_frame_rate(16000)

        # Export as WAV
        audio.export(wav_path, format='wav')

        print(f"Converted {mp3_file} to {wav_file}")

        # Delete the MP3 fil
        os.remove(mp3_path)
        print(f"Deleted {mp3_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python mp3_to_wav_converter.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print("Invalid directory path.")
        sys.exit(1)

    convert_mp3_to_wav(directory)