import os

txt_dir = '../txt/'
BASE_CHORDS = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']

choords = set()

for filename in os.listdir(txt_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(txt_dir, filename), 'r') as txt_file:
            lines = txt_file.readlines()
            for line in lines:
                line = line.strip()
                if len(line.strip()) > 2:
                    chord = line[0] + line[1]
                    if chord in BASE_CHORDS:
                        found = line.split(" ")
                        for f in found:
                            choords.add(f.strip())
print(choords)
