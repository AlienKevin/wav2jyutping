import pandas as pd
import os
import shutil
from pathlib import Path

# Instructions: https://huggingface.co/docs/datasets/audio_dataset#audiofolder

input_dir = Path("yue")/"clips"
output_dir = Path("yue")/"data"

os.makedirs(output_dir/"train", exist_ok=True)
os.makedirs(output_dir/"test", exist_ok=True)

df = pd.read_csv("test.csv")
for id, row in df.iterrows():
    shutil.copy(input_dir/(row["file_name"] + ".mp3"), output_dir/"test")

df = pd.read_csv("train.csv")
for id, row in df.iterrows():
    shutil.copy(input_dir/(row["file_name"] + ".mp3"), output_dir/"train")

df = pd.read_csv("other.csv")
for id, row in df.iterrows():
    shutil.copy(input_dir/(row["file_name"] + ".mp3"), output_dir/"train")
