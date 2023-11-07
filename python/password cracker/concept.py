# Specify the file path
file_path = "E:/rockyou/RockYou2021.txt/rockyou2021.lst"

# Initialize a variable to store the line
line_from_file = None

# Open the file and read the desired line (e.g., line 3)
with open(file_path, "r") as file:
    # Use the line number you want (subtract 1 because Python uses 0-based indexing)
    line_number = 3  # Change this to the desired line number
    lines = file.readlines()
    
    if 0 <= line_number < len(lines):
        line_from_file = lines[line_number].strip()

# Check if a line was successfully read from the file
if line_from_file is not None:
    print("Line from file:", line_from_file)
else:
    print("Line number is out of range.")

