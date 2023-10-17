import pandas as pd
import os 

def format_df(train_df):
  """Preprocesses a train dataframe for speech recognition.

  Args:
    train_df: A Pandas dataframe with the following columns:
      * client_id
      * path
      * sentence
      * up_votes
      * down_votes
      * age
      * gender
      * accents
      * variant
      * locale
      * segment

  Returns:
    A Pandas dataframe with the following columns:
      * wav_filename
      * wav_filesize
      * transcript
  """

  # Create a new dataframe with the specified columns.
  new_df = pd.DataFrame(columns=["wav_filename", "wav_filesize", "transcript"])

  # Iterate over the rows of the train dataframe.
  for index, row in train_df.iterrows():

    # Get the path to the waveform file.
    wav_filepath = row["path"]

    # Get the filename of the waveform file.
    wav_filename = wav_filepath.split("/")[-1]

    # Add the prefix .wav to the filename.
    wav_filename = wav_filename.replace(".mp3", "") + ".wav"


    # Get the size of the waveform file in bytes.
    wav_filesize = os.path.getsize(wav_filepath)

    # Get the transcript of the waveform file.
    transcript = row["sentence"]

    # Add a new row to the new dataframe.
    new_df.loc[index] = [f"train/{wav_filename}", wav_filesize, transcript]

  return new_df
