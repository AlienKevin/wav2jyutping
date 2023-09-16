import os
import csv
import ToJyutping

def build_transcription(input_path, transcription_path) -> list[str]:
    with open(input_path, 'r', encoding='utf-8') as input, \
        open(transcription_path, 'w+', encoding='utf-8') as transcription:
        reader = csv.reader(input, delimiter='\t')
        # skip header row
        next(reader)

        audio_paths = []

        transcription.write("transcription,file_name\n")

        for row in reader:
            audio_path = row[1]
            filename = os.path.basename(audio_path).removesuffix(".mp3")
            audio_paths.append(audio_path)
            # Ignore tones
            jyutpings = " ".join([jyutping[:-1] for (_, jyutping) in ToJyutping.get_jyutping_list(row[2]) if jyutping is not None])
            transcription.write(f"{jyutpings},{filename}\n")
        
        return audio_paths

if __name__ == '__main__':
    # build_transcription("yue/other.tsv", "other.csv")
    # build_transcription("data/test.tsv", "test.csv")
    build_transcription("zh-HK/validated.tsv", "validated-zh-HK.csv")
