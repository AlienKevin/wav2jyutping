import utils

total_errors = 0

with open("whisper-base-jyutping-without-tones-full-test-wrong.txt", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        if utils.merge_sounds(lines[i]) != utils.merge_sounds(lines[i + 1]):
            total_errors += 1

print("Total errors:", total_errors)
