
import sys
sys.path.append("")
import os
import rpatool

def main():
    # Create a new archive instance
    archive = rpatool.RenPyArchive(version=3)
    
    # Path to the extracted files directory
    extracted_dir = "temp_rpa_extraction"
    
    # Add all the extracted files to the archive
    for root, _, files in os.walk(extracted_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, extracted_dir)
            with open(file_path, 'rb') as f:
                content = f.read()
                archive.add(relative_path, content)
    
    # Save the archive to a new RPA file
    archive.save("archive.rpa")

if __name__ == '__main__':
    main()
