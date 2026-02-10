import os

files = os.listdir("files")

for file in files:
    parts = file.split('_')
    part1 = parts[1]
    part2 = parts[2].replace('.txt',"")

    new_name = f"{part1}_{part2}_marks.txt"

    old_file_path = os.path.join("files", file)
    new_file_path = os.path.join("files", new_name)
    
    os.rename(old_file_path, new_file_path)