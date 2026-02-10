import os

files = os.listdir("files")

for file in files:
    parts = file.split('_')
    part1 = parts[1]
    part2 = parts[2].replace('.txt',"")

    new_name = f"{part1}_{part2}_marks.txt"

    os.rename(f"old name: /{file}", "new name:/{new_name}")