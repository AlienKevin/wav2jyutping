import pandas as pd
import re

# https://stackoverflow.com/a/6117042/6798201
def sub_all(text, pats):
    for pat, rep in pats.items():
        text = re.sub(pat, rep, text)
    return text

def merge_sounds(jyutpings: str) -> str:
    """
    >>> merge_sounds("gwong dung waa")
    'gon dung waa'
    >>> merge_sounds("ngo sing ngok")
    'o sing ot'
    >>> merge_sounds("nei ng hai ngo uk kei jan")
    'lei m hai o uk kei jan'
    >>> merge_sounds("ga la")
    'gaa laa'
    """
    return " ".join((
        sub_all(jyutping, {"^ng$": "m", "^ng([a-z])": r"\1", "^n([^g])": r"l\1", "^([kg])wo": r"\1o", "([^iu])ng$": r"\1n", "ok$": "ot", "([^a]|^)a$": r"\1aa"})
        for jyutping in jyutpings.split(" ")))

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
            merged = merge_sounds(row["transcription"])
            syllable_set_merged.update(merged.split(" "))
            output.write(row["file_name"] + "," + merged + "\n")
    
    print("Original syllables:", len(syllable_set_original))
    print("Merged syllables:", len(syllable_set_merged))
