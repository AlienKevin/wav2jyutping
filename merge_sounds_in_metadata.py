import pandas as pd
import utils

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    syllable_set_original = set()
    syllable_set_merged = set()

    with open("yue/metadata.csv", "w+") as output:
        output.write("file_name,transcription\n")
        df = pd.read_csv("yue/metadata_original.csv")
        for id, row in df.iterrows():
            syllable_set_original.update(row["transcription"].split(" "))
            merged = utils.merge_sounds(row["transcription"])
            syllable_set_merged.update(merged.split(" "))
            output.write(row["file_name"] + "," + merged + "\n")
    
    print("Original syllables:", len(syllable_set_original))
    print("Merged syllables:", len(syllable_set_merged))
