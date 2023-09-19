import pandas as pd
from pathlib import Path
import os
import ToJyutping

transcripts = set()

# with open("mdcc/metadata.csv", "w+") as output:
#     output.write("file_name,transcription\n")
df = pd.read_csv("mdcc/cnt_asr_metadata_full.csv")
for id, row in df.iterrows():
    transcript = (Path("mdcc")/row["text_path"]).read_text()
    if transcript not in transcripts:
        transcripts.add(transcript)
        jyutping = " ".join([jyutping[:-1] for (_, jyutping) in ToJyutping.get_jyutping_list(transcript) if jyutping is not None])
        if len(jyutping) > 0:
            # output.write((Path("audio")/os.path.basename(row["audio_path"])).as_posix() + "," + jyutping + "\n")
            pass
        else:
            p = Path("all/data/train")/(row["text_path"].removeprefix("audio/").replace("/transcription/", "/").removesuffix(".txt") + ".wav")
            print(p)
            os.remove(p)
