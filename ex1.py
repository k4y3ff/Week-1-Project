import os
import shutil

# # Create 26 directories in the current directory, one for each letter of the alphabet.
 for num in range(97, 123):
 	if not os.path.exists(chr(num)):
 		os.makedirs(chr(num))

# Get the path of the current python file running (ex1.py).
python_file_dir, python_file_name = os.path.split(os.path.abspath(__file__))

# Get a list of all files in the original_files directory.
original_files_path = python_file_dir + "/original_files"
file_list = os.listdir(original_files_path)

# Loop through all files in the original_files directory, placing each in its proper
# directory in the current directory depending on the first character of its filename.
for item in file_list:
	if 97 <= ord(item[:1].lower()) <= 122:
		shutil.move(original_files_path + "/" + item, python_file_dir + "/" + item[:1].lower())