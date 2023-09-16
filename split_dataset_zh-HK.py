import pandas as pd
import os
import shutil
from pathlib import Path

# Instructions: https://huggingface.co/docs/datasets/audio_dataset#audiofolder

input_dir = Path("zh-HK")/"clips"
output_dir = Path("zh-HK")/"data"

os.makedirs(output_dir/"train", exist_ok=True)
os.makedirs(output_dir/"test", exist_ok=True)

yue_data_sentences = set()

df = pd.read_csv("test.csv")
for id, row in df.iterrows():
    yue_data_sentences.add(row["transcription"])
df = pd.read_csv("other.csv")
for id, row in df.iterrows():
    yue_data_sentences.add(row["transcription"])
df = pd.read_csv("train.csv")
for id, row in df.iterrows():
    yue_data_sentences.add(row["transcription"])

df = pd.read_csv("test.csv")
for id, row in df.iterrows():
    shutil.copy(Path("yue")/"clips"/(row["file_name"] + ".mp3"), output_dir/"test")

df = pd.read_csv("validated-zh-HK.csv")
for id, row in df.iterrows():
    if row["transcription"] not in yue_data_sentences:
        shutil.copy(input_dir/(row["file_name"] + ".mp3"), output_dir/"train")
