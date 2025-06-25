import os

# Step 1: Get all .py files in the current directory
files = [f for f in os.listdir() if f.endswith(".py")]

# Step 2: Sort them alphabetically
files.sort()

# Step 3: Rename each file with [01], [02], etc.
for i, file in enumerate(files):
    number = f"[{i + 1:02}]"

    # Remove old prefix like [12] if present
    name = file
    if name.startswith('[') and ']' in name:
        name = name.split('] ', 1)[1]

    new_name = f"{number} {name}"

    if new_name != file:  # Avoid unnecessary renaming
        print(f"Renaming: {file} -> {new_name}")
        os.rename(file, new_name)
