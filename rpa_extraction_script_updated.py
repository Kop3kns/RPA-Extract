
import sys
sys.path.append('')
import os
import rpatool

class CustomRenPyArchive(rpatool.RenPyArchive):
    def extract_all(self, output_dir):
        # Extract all files from the archive
        for filename in self.list():
            content = self.read(filename)
            file_path = os.path.join(output_dir, filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(content)

def main():
    archive = CustomRenPyArchive("setupRPC.rpa")
    archive.extract_all("temp_rpa_extraction")

if __name__ == '__main__':
    main()
