with open("whisper-base-jyutping-without-tones-full-test-output.txt", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        if lines[i] != lines[i + 1]:
            print(lines[i].strip())
            print(lines[i + 1].strip())
            print()
