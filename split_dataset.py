import pandas as pd
import os
import shutil
from pathlib import Path

# Instructions: https://huggingface.co/docs/datasets/audio_dataset#audiofolder

data_dir = Path("yue_common_voice"/"data")

os.makedirs(data_dir/"train", exist_ok=True)
os.makedirs(data_dir/"test", exist_ok=True)

df = pd.read_csv("test.csv")
for id, row in df.iterrows():
    shutil.copy(data_dir/(row["file_name"] + ".wav"), data_dir/"test")

df = pd.read_csv("train.csv")
for id, row in df.iterrows():
    shutil.copy(data_dir/(row["file_name"] + ".wav"), data_dir/"train")
