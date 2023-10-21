import pandas as pd
import os 

def format_df(df, label):
    """Preprocesses a train dataframe for speech recognition.

    Args:
        df: A Pandas dataframe with the following columns:
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
        label: A string representing the label.

    Returns:
        A Pandas dataframe with the following columns:
            * wav_filename
            * wav_filesize
            * transcript
    """
    # Check if the dataframe is already formatted and if PATH names match label
    if "wav_filename" in df.columns and "wav_filesize" in df.columns and "transcript" in df.columns:
        print('Format acceptable: checking clip directories')
        for i in range(len(df)):
            current_entry = df.loc[i, 'wav_filename']
            entry_parts = current_entry.split("/")
            file_name = entry_parts[1]
            current_label = entry_parts[0]
            if current_label != label:
                current_label = label
                new_entry = f"{label}/{file_name}"
                df.loc[i, 'wav_filename'] = new_entry
        return df  # Return the modified dataframe outside the loop

    else:
        # Create a new dataframe with the specified columns.
        new_df = pd.DataFrame(columns=["wav_filename", "wav_filesize", "transcript"])

        # Iterate over the rows of the train dataframe.
        for index, row in df.iterrows():
            # Get the path to the waveform file.
            wav_filepath = row["path"]

            # Get the filename of the waveform file.
            wav_filename = wav_filepath.split("/")[-1]

            # Get the size of the waveform file in bytes.
            wav_filesize = os.path.getsize(wav_filepath)

            # Get the transcript of the waveform file.
            transcript = row["sentence"]

            # Add a new row to the new dataframe.
            new_df.loc[index] = [f"{label}/{wav_filename}", wav_filesize, transcript]

        return new_df

