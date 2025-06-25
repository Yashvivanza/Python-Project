import os

# Get all Python files and sort them alphabetically
files = sorted([f for f in os.listdir() if f.endswith(".py")])

for i, file in enumerate(files):
    # Format number with leading zeros like [01], [02], ...
    new_name = f"[{i + 1:02}] {file}"

    # Remove existing prefix if already renamed before
    if file.startswith("[") and "]" in file:
        original_name = file.split("] ", 1)[1]
        new_name = f"[{i + 1:02}] {original_name}"

    os.rename(file, new_name)
