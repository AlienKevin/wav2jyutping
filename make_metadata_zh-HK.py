import pandas as pd
from pathlib import Path

# Instructions: https://huggingface.co/docs/datasets/audio_dataset#audiofolder

data_dir = Path("data")

with open("zh-HK/metadata.csv", "w+") as output:
    output.write("file_name,transcription\n")
    yue_data_sentences = set()
    df = pd.read_csv("test.csv")
    for id, row in df.iterrows():
        yue_data_sentences.add(row["transcription"])
        output.write((data_dir/"test"/(row["file_name"] + ".mp3")).as_posix() + "," + row["transcription"] + "\n")
    
    df = pd.read_csv("other.csv")
    for id, row in df.iterrows():
        yue_data_sentences.add(row["transcription"])
    df = pd.read_csv("train.csv")
    for id, row in df.iterrows():
        yue_data_sentences.add(row["transcription"])

    df = pd.read_csv("validated-zh-HK.csv")
    for id, row in df.iterrows():
        if row["transcription"] not in yue_data_sentences:
            output.write((data_dir/"train"/(row["file_name"] + ".mp3")).as_posix() + "," + row["transcription"] + "\n")
        else:
            print("Found duplicated sentence " + row["transcription"])
