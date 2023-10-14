import pandas as pd
import json
import tqdm
import argparse

parser = argparse.ArgumentParser("MCV TSV-to-JSON converter")
parser.add_argument("--tsv", required=True, type=str, help="Input TSV file")
parser.add_argument("--sampling_count", required=True, type=int, help="Number of examples, you want, use -1 for all examples")
parser.add_argument("--folder", required=True, type=str, help="Relative path to folder with audio files")
args = parser.parse_args()

df = pd.read_csv(args.tsv, sep='\t')
with open(args.tsv.replace('.tsv', '.json'), 'w') as fo:
    mod = 1
    if args.sampling_count > 0:
        mod = len(df) // args.sampling_count
    for idx in tqdm.tqdm(range(len(df))):
        if idx % mod != 0:
            continue
        item = {
            'audio_filepath': args.folder + "/" + df['path'][idx],
            'text': df['sentence'][idx],
            'up_votes': int(df['up_votes'][idx]), 'down_votes': int(df['down_votes'][idx]),
            'age': df['age'][idx], 'gender': df['gender'][idx], 'accents': df['accents'][idx],
            'client_id': df['client_id'][idx]
        }
        fo.write(json.dumps(item) + "\n")