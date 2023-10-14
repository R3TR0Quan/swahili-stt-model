# Mozilla Common Voice Speech-to-Text Hackathon
This repository contains code worked on during the Mozilla Common Voice hackathon hosted by Africa's Talking on Oct 13th 2023

## The Data
The data used was sourced by Mozilla in a crowd sourcing activity spanning several years. The latest version can be found [here](https://commonvoice.mozilla.org/en/datasets)

We converted the `tsv` files to `json` for compatibility with **Nvidia Nemo**. If using **Coqui-stt** `csv` is required and you would need a different script to achieve the conversion

To convert tsv to json run:
`python tsv_to_json.py \ --tsv=sw/train.tsv \ --folder=sw/clips \ --sampling_count=-1`

To convert the mp3 files to wav run:
`python scripts/decode_resample.py   --manifest=sw/train.json   --destination_folder=./train`

Do this for train, dev and test data sets
## Replicating results

The current version of Coqui-STT used in this project depends on Tensorflow 1.15.4. To replicate create a new env in python3.7 and install the packages in *requirements.txt*

`pip install -r requirements.txt`
