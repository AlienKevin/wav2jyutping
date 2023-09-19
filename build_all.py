import pandas as pd
import os
from pathlib import Path
import shutil

root_dir = Path("all")
data_dir = root_dir/"data"
train_dir = data_dir/"train"
test_dir = data_dir/"test"

# os.makedirs(train_dir)
# os.makedirs(test_dir)

metadata = []

def skip_first_dir(path):
    return Path(*Path(path).parts[1:])

df = pd.read_csv("mdcc/metadata.csv", keep_default_na=False)
for id, row in df.iterrows():
    # shutil.copy(Path("mdcc")/row["file_name"], train_dir/skip_first_dir(row["file_name"]))
    metadata.append(((Path("data/train")/(skip_first_dir(row["file_name"]))).as_posix(), row["transcription"], 0))

df = pd.read_csv("zh-HK/metadata.csv", keep_default_na=False)
for id, row in df.iterrows():
    if row["file_name"].startswith("data/train"):
        # shutil.copy(Path("zh-HK")/row["file_name"], root_dir/row["file_name"])
        metadata.append((row["file_name"], row["transcription"], 1))

df = pd.read_csv("yue/metadata.csv", keep_default_na=False)
for id, row in df.iterrows():
    if row["file_name"].startswith("data/train"):
        # shutil.copy(Path("yue")/row["file_name"], root_dir/row["file_name"])
        metadata.append((row["file_name"], row["transcription"], 2))
    else:
        # shutil.copy(Path("yue")/row["file_name"], root_dir/row["file_name"])
        metadata.append((row["file_name"], row["transcription"], 2))

with open(root_dir/"metadata.csv", "w+") as output:
    output.write("file_name,transcription,sequence\n")
    for file, transcription, sequence in metadata:
        output.write(file + "," + transcription + "," + str(sequence) + "\n")
