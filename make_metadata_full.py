import pandas as pd
from pathlib import Path

# Instructions: https://huggingface.co/docs/datasets/audio_dataset#audiofolder

data_dir = Path("data")

with open("yue/metadata.csv", "w+") as output:
    output.write("file_name,transcription\n")
    df = pd.read_csv("test.csv")
    for id, row in df.iterrows():
        output.write((Path("data")/"test"/(row["file_name"] + ".mp3")).as_posix() + "," + row["transcription"] + "\n")
    df = pd.read_csv("train.csv")
    for id, row in df.iterrows():
        output.write((Path("data")/"train"/(row["file_name"] + ".mp3")).as_posix() + "," + row["transcription"] + "\n")
    df = pd.read_csv("other.csv")
    for id, row in df.iterrows():
        output.write((Path("data")/"train"/(row["file_name"] + ".mp3")).as_posix() + "," + row["transcription"] + "\n")
